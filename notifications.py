"""
notifications.py — Pluggable notification channels for IT Tasker.

Each channel exposes a single ``send(subject, body, **kwargs)`` function.
The ``notify_ticket`` helper picks the right channels based on config and
fires them in turn.  Failures are logged but never bubble up to the caller
so ticket creation is never blocked by a notification error.
"""

import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.request import Request, urlopen
from urllib.error import URLError
import json

import config

log = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────────────────────────
# Email (SMTP)
# ──────────────────────────────────────────────────────────────────────────────

def send_email(to_address: str, subject: str, body: str) -> bool:
    """Send a plain-text email via SMTP.  Returns True on success."""
    if not to_address:
        return False
    try:
        msg = MIMEMultipart("alternative")
        msg["From"] = config.EMAIL_FROM
        msg["To"] = to_address
        msg["Subject"] = f"{config.EMAIL_SUBJECT_PREFIX} {subject}"
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(config.EMAIL_SMTP_HOST, config.EMAIL_SMTP_PORT, timeout=15) as srv:
            if config.EMAIL_USE_TLS:
                srv.starttls()
            if config.EMAIL_USERNAME:
                srv.login(config.EMAIL_USERNAME, config.EMAIL_PASSWORD)
            srv.sendmail(config.EMAIL_FROM, [to_address], msg.as_string())
        log.info("Email sent to %s — %s", to_address, subject)
        return True
    except Exception:
        log.exception("Failed to send email to %s", to_address)
        return False


# ──────────────────────────────────────────────────────────────────────────────
# Discord Webhook
# ──────────────────────────────────────────────────────────────────────────────

def send_discord(subject: str, body: str) -> bool:
    """Post a message to a Discord channel via webhook.  Returns True on success."""
    url = config.DISCORD_WEBHOOK_URL
    if not url:
        return False
    try:
        mention = ""
        if config.DISCORD_MENTION_ROLE:
            mention = f"<@&{config.DISCORD_MENTION_ROLE}> "

        payload = {
            "username": config.DISCORD_BOT_NAME,
            "content": f"{mention}**{subject}**\n{body}",
        }
        data = json.dumps(payload).encode("utf-8")
        req = Request(url, data=data, headers={"Content-Type": "application/json"})
        urlopen(req, timeout=15)
        log.info("Discord notification sent — %s", subject)
        return True
    except (URLError, OSError):
        log.exception("Failed to send Discord notification")
        return False


# ──────────────────────────────────────────────────────────────────────────────
# Unified dispatcher
# ──────────────────────────────────────────────────────────────────────────────

def notify_ticket(ticket_type: str, action: str, description: str,
                  contact_email: str = "", **extra):
    """Fire all enabled notification channels for a ticket event.

    Args:
        ticket_type: e.g. "Walk-in Ticket", "Escalated Ticket"
        action:      e.g. "created", "updated", "resolved"
        description: The ticket description text.
        contact_email: Optional email to notify the affected user.
        **extra:     Additional context (reported_by, ticket_number, etc.)
    """
    if not config.NOTIFICATIONS_ENABLED:
        return

    subject = f"{ticket_type} {action}"
    lines = [f"Type: {ticket_type}", f"Action: {action}"]
    for key, val in extra.items():
        if val:
            lines.append(f"{key.replace('_', ' ').title()}: {val}")
    lines.append(f"Description: {description}")
    body = "\n".join(lines)

    # Email to the affected user (contact_email on the ticket)
    if config.EMAIL_ENABLED and contact_email:
        send_email(contact_email, subject, body)

    # Discord channel notification
    if config.DISCORD_ENABLED:
        send_discord(subject, body)
