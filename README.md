# IT Tasker

A lightweight, configurable **IT ticket tracker** built with Flask and SQLite. Designed as a drop-in solution for small IT teams that need a simple way to log walk-in requests and escalated incidents without the overhead of a full ITSM platform.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- **Walk-in / Phone-in Tickets** — Log day-to-day requests from users who walk in or call.
- **Escalated Tickets** — Track issues raised with an external helpdesk or vendor (ServiceNow, Jira, Zendesk, etc.).
- **Dashboard** — At-a-glance stats, quick-entry buttons, and recent ticket tables.
- **Reporting** — Date-range summary reports exported in-browser, plus optional R/ggplot2 analytics charts.
- **Excel Import** — Bulk-import tickets from an `.xlsx` file.
- **Multi-user Auth** — Simple username/password login with an admin user-management page.
- **Dark Mode** — Toggle between light and dark themes (saved in localStorage).
- **Fully Configurable** — One `config.py` file controls branding, labels, icons, colours, statuses, and more.

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/<you>/it-tasker.git
cd it-tasker

# 2. Install dependencies
pip install flask flask-login werkzeug openpyxl

# 3. (Optional) Install R + ggplot2 for analytics charts
# brew install r          # macOS
# Rscript -e 'install.packages(c("ggplot2","scales"))'

# 4. Run
python app.py
```

Open **http://127.0.0.1:5001** — default login is `admin` / `admin123`.

> **Change the default password immediately** via the Change Password page.

## Configuration

All settings live in [`config.py`](config.py). Edit it to match your organisation:

| Setting | Default | Purpose |
|---|---|---|
| `APP_NAME` | `"IT Tasker"` | Navbar, login page, page titles |
| `APP_ICON` | `"bi bi-shield-check"` | [Bootstrap Icon](https://icons.getbootstrap.com/) class |
| `APP_COLOUR` | `"#1a3a5c"` | Primary header / navbar colour |
| `WALKIN_LABEL` | `"Walk-in Tickets"` | Sidebar & heading for walk-in tickets |
| `ESCALATED_LABEL` | `"Escalated Tickets"` | Sidebar & heading for escalated tickets |
| `ESCALATED_SYSTEM_NAME` | `"Ticket"` | The name of your external ticket system |
| `ESCALATED_NUMBER_LABEL` | `"Ticket Number"` | Label for the external ticket ID field |
| `STATUSES` | `["IN PROGRESS", "RESOLVED"]` | Ticket status options |
| `SECRET_KEY` | `"change-me-..."` | Flask session key — **change for production** |
| `DATABASE_NAME` | `"it_tasker.db"` | SQLite database filename |
| `PORT` | `5001` | Server port |

See the file for the full list of options.

## Project Structure

```
├── app.py           # Flask routes and business logic
├── config.py        # All configurable settings
├── models.py        # SQLite schema and database helpers
├── report.R         # Optional R analytics chart generator
├── templates/       # Jinja2 HTML templates (Bootstrap 5)
└── README.md
```

## Tech Stack

- **Backend** — Python 3, Flask, Flask-Login
- **Database** — SQLite (WAL mode, zero config)
- **Frontend** — Bootstrap 5.3, Bootstrap Icons, vanilla JS
- **Analytics** — R + ggplot2 (optional)

## License

MIT
