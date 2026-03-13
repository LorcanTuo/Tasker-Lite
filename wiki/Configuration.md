# Configuration

All settings are in `config.py`. Changes take effect on restart (or immediately in debug mode on save).

## Branding

| Setting | Default | Purpose |
|---|---|---|
| `APP_NAME` | `"IT Tasker"` | Shown in the navbar, login page, and page titles |
| `APP_ICON` | `"bi bi-shield-check"` | [Bootstrap Icon](https://icons.getbootstrap.com/) class for the logo |
| `APP_COLOUR` | `"#1a3a5c"` | Primary navbar/header colour (light mode) |
| `APP_COLOUR_DARK` | `"#0d1f33"` | Navbar colour in dark mode |

### Choosing an icon

Browse the [Bootstrap Icons gallery](https://icons.getbootstrap.com/) and copy the class name (e.g. `bi bi-laptop`).

## Server

| Setting | Default | Purpose |
|---|---|---|
| `HOST` | `"127.0.0.1"` | Bind address (`"0.0.0.0"` to allow external access) |
| `PORT` | `5001` | HTTP port |
| `DEBUG` | `True` | Enable Flask debug mode (set to `False` in production) |
| `SECRET_KEY` | `"change-me-to-something-random"` | Flask session signing key — **change this for production** |

### Generating a secret key

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and paste it as the `SECRET_KEY` value.

## Walk-in Tickets

| Setting | Default | Purpose |
|---|---|---|
| `WALKIN_LABEL` | `"Walk-in Tickets"` | Sidebar link and page heading |
| `WALKIN_LABEL_SINGULAR` | `"Walk-in Ticket"` | Used in flash messages |
| `WALKIN_ICON` | `"bi bi-person-walking"` | Bootstrap Icon class |
| `WALKIN_ROUTE_PREFIX` | `"walkin"` | URL prefix (e.g. `/walkin`, `/walkin/new`) |

## Escalated Tickets

| Setting | Default | Purpose |
|---|---|---|
| `ESCALATED_LABEL` | `"Escalated Tickets"` | Sidebar link and page heading |
| `ESCALATED_LABEL_SINGULAR` | `"Escalated Ticket"` | Used in flash messages |
| `ESCALATED_ICON` | `"bi bi-exclamation-triangle"` | Bootstrap Icon class |
| `ESCALATED_ROUTE_PREFIX` | `"escalated"` | URL prefix |
| `ESCALATED_SYSTEM_NAME` | `"Ticket"` | Name of your external ticket system (e.g. `"ServiceNow"`, `"Jira"`) |
| `ESCALATED_NUMBER_LABEL` | `"Ticket Number"` | Label for the external ticket ID field (e.g. `"INC Number"`) |
| `ESCALATED_DATE_LABEL` | `"Escalation Date"` | Label for the escalation date field |
| `ESCALATED_RAISED_BY_LABEL` | `"Escalated By"` | Label for who raised the escalation |

### Example: ServiceNow configuration

```python
ESCALATED_SYSTEM_NAME    = "ServiceNow"
ESCALATED_NUMBER_LABEL   = "INC Number"
ESCALATED_DATE_LABEL     = "ServiceNow Date"
ESCALATED_RAISED_BY_LABEL = "Raised By"
```

## Statuses

| Setting | Default | Purpose |
|---|---|---|
| `STATUSES` | `["IN PROGRESS", "RESOLVED"]` | Status options shown in ticket forms |

You can add additional statuses by extending the list:

```python
STATUSES = ["IN PROGRESS", "ON HOLD", "WAITING ON USER", "RESOLVED"]
```

## Database

| Setting | Default | Purpose |
|---|---|---|
| `DATABASE_NAME` | `"it_tasker.db"` | SQLite database filename (created alongside `app.py`) |

The database is created automatically on first run. See [[Database Schema]] for the table structure.
