# ──────────────────────────────────────────────────────────────────────────────
# IT Tasker — Configuration
# ──────────────────────────────────────────────────────────────────────────────
# Edit this file to customise the app for your team.
# Changes take effect on restart (or immediately in debug mode on save).
# ──────────────────────────────────────────────────────────────────────────────

# ── Branding ──────────────────────────────────────────────────────────────────
APP_NAME = "IT Tasker"                     # Shown in navbar, login page, titles
APP_ICON = "bi bi-shield-check"            # Bootstrap Icon class for the logo
APP_COLOUR = "#1a3a5c"                     # Primary navbar / header colour
APP_COLOUR_DARK = "#0d1f33"                # Navbar colour in dark mode

# ── Secret key (change this for production!) ──────────────────────────────────
SECRET_KEY = "change-me-to-something-random"

# ── Server ────────────────────────────────────────────────────────────────────
HOST = "127.0.0.1"
PORT = 5001
DEBUG = True

# ── Walk-in Tickets (daily / phone-in / walk-in requests) ────────────────────
WALKIN_LABEL = "Walk-in Tickets"           # Sidebar & page heading
WALKIN_LABEL_SINGULAR = "Walk-in Ticket"   # Used in flash messages
WALKIN_ICON = "bi bi-person-walking"       # Bootstrap Icon class
WALKIN_ROUTE_PREFIX = "walkin"             # URL prefix, e.g. /walkin, /walkin/new

# ── Escalated Tickets (incidents raised with external helpdesk / vendor) ─────
ESCALATED_LABEL = "Escalated Tickets"
ESCALATED_LABEL_SINGULAR = "Escalated Ticket"
ESCALATED_ICON = "bi bi-exclamation-triangle"
ESCALATED_ROUTE_PREFIX = "escalated"

# Customise the "ticket system" field labels for escalated tickets.
# For example, if your org uses ServiceNow, Jira Service Desk, Zendesk, etc.
ESCALATED_SYSTEM_NAME = "Ticket"           # e.g. "AHD", "ServiceNow", "Jira"
ESCALATED_NUMBER_LABEL = "Ticket Number"   # e.g. "AHD Number", "INC Number"
ESCALATED_DATE_LABEL = "Escalation Date"   # e.g. "AHD Date"
ESCALATED_RAISED_BY_LABEL = "Escalated By" # e.g. "AHD Raised By"

# ── Statuses ──────────────────────────────────────────────────────────────────
STATUSES = ["IN PROGRESS", "RESOLVED"]

# ── Database ──────────────────────────────────────────────────────────────────
DATABASE_NAME = "it_tasker.db"             # SQLite file, created alongside app.py
