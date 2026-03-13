# IT Tasker

A lightweight, configurable **IT ticket tracker** built with Flask and SQLite. Designed as a drop-in solution for small IT teams that need a simple way to log walk-in requests and escalated incidents without the overhead of a full ITSM platform.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

> **📖 [Full documentation available on the Wiki](https://github.com/LorcanTuo/Tasker-Lite/wiki)**

> **⚠️ Experimental Branch (`docker`)** — This branch adds Docker support for containerised deployment. These changes are experimental and may be subject to change or removal. Do not rely on this setup for production without thorough testing.

## What's New on This Branch

- **Dockerfile** — Python 3.12-slim image with a non-root user and built-in healthcheck.
- **docker-compose.yml** — Single-command deployment with a named volume for database persistence.
- **Environment Variable Config** — `SECRET_KEY`, `HOST`, `PORT`, and `DEBUG` can now be set via environment variables (falls back to `config.py` defaults for local dev).
- **Volume-Mounted Database** — The SQLite database path is configurable via `DATABASE_PATH` so data survives container restarts.

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

### Local Development

```bash
# 1. Clone the repo
git clone https://github.com/LorcanTuo/Tasker-Lite.git
cd Tasker-Lite

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Install R + ggplot2 for analytics charts
# brew install r          # macOS
# Rscript -e 'install.packages(c("ggplot2","scales"))'

# 4. Run
python app.py
```

### Docker

```bash
# Build and run with Docker Compose
docker compose up -d

# Or build and run manually
docker build -t it-tasker .
docker run -d -p 5001:5001 \
  -e SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))") \
  -e HOST=0.0.0.0 \
  -e DEBUG=false \
  -v tasker-data:/app/data \
  it-tasker
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

### Environment Variables (this branch only)

When running in Docker (or any environment), the following settings can be overridden via environment variables:

| Variable | Default | Purpose |
|---|---|---|
| `SECRET_KEY` | `"change-me-to-something-random"` | Flask session signing key |
| `HOST` | `"127.0.0.1"` | Bind address (`0.0.0.0` for Docker) |
| `PORT` | `5001` | HTTP port |
| `DEBUG` | `"true"` | Enable debug mode (`"false"` for production) |
| `DATABASE_PATH` | App directory | Directory for the SQLite database file |

## Project Structure

```
├── app.py              # Flask routes and business logic
├── config.py           # All configurable settings (env var aware)
├── models.py           # SQLite schema and database helpers
├── requirements.txt    # Python dependencies
├── report.R            # Optional R analytics chart generator
├── Dockerfile          # Container image definition
├── docker-compose.yml  # Single-command container deployment
├── .dockerignore       # Files excluded from the Docker build
├── templates/          # Jinja2 HTML templates (Bootstrap 5)
└── README.md
```

## Tech Stack

- **Backend** — Python 3, Flask, Flask-Login
- **Database** — SQLite (WAL mode, zero config)
- **Frontend** — Bootstrap 5.3, Bootstrap Icons, vanilla JS
- **Analytics** — R + ggplot2 (optional)

## Wiki

For detailed guides, visit the **[Wiki](https://github.com/LorcanTuo/Tasker-Lite/wiki)**:

- [Getting Started](https://github.com/LorcanTuo/Tasker-Lite/wiki/Getting-Started) — Installation and first run
- [Configuration](https://github.com/LorcanTuo/Tasker-Lite/wiki/Configuration) — Customise branding, labels, statuses, and more
- [Walk-in Tickets](https://github.com/LorcanTuo/Tasker-Lite/wiki/Walk-in-Tickets) — Creating and managing walk-in tickets
- [Escalated Tickets](https://github.com/LorcanTuo/Tasker-Lite/wiki/Escalated-Tickets) — Tracking externally escalated issues
- [Reports and Analytics](https://github.com/LorcanTuo/Tasker-Lite/wiki/Reports-and-Analytics) — Generating reports and R charts
- [User Management](https://github.com/LorcanTuo/Tasker-Lite/wiki/User-Management) — Adding users and changing passwords
- [Import and Export](https://github.com/LorcanTuo/Tasker-Lite/wiki/Import-and-Export) — Bulk importing and exporting ticket data
- [Database Schema](https://github.com/LorcanTuo/Tasker-Lite/wiki/Database-Schema) — SQLite table structure and indexes

## License

MIT
