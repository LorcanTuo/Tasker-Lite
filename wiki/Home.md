# IT Tasker Wiki

Welcome to the **IT Tasker** wiki — a lightweight IT ticket tracker built with Flask and SQLite.

IT Tasker is designed as a drop-in solution for small IT teams that need a simple way to log walk-in requests and escalated incidents without the overhead of a full ITSM platform.

## Key Features

| Feature | Description |
|---|---|
| **Walk-in Tickets** | Log day-to-day requests from users who walk in or call |
| **Escalated Tickets** | Track issues raised with an external helpdesk or vendor |
| **Dashboard** | At-a-glance stats, quick-entry buttons, and recent ticket tables |
| **Reporting** | Date-range summary reports with optional R/ggplot2 analytics charts |
| **Excel Import/Export** | Bulk-import tickets from `.xlsx` or export reports to Excel |
| **Multi-user Auth** | Username/password login with admin user management |
| **Dark Mode** | Toggle between light and dark themes |
| **Fully Configurable** | One `config.py` file controls branding, labels, icons, colours, and more |

## Tech Stack

- **Backend** — Python 3.8+, Flask 3.x, Flask-Login
- **Database** — SQLite (WAL mode, zero config)
- **Frontend** — Bootstrap 5.3, Bootstrap Icons, vanilla JS
- **Analytics** — R + ggplot2 (optional)

## Quick Links

- [[Getting Started]] — Installation and first run
- [[Configuration]] — Customise branding, labels, statuses, and more
- [[Walk-in Tickets]] — Creating and managing walk-in tickets
- [[Escalated Tickets]] — Tracking externally escalated issues
- [[Reports and Analytics]] — Generating reports and R charts
- [[User Management]] — Adding users and changing passwords
- [[Import and Export]] — Bulk importing and exporting ticket data
- [[Database Schema]] — SQLite table structure and indexes
