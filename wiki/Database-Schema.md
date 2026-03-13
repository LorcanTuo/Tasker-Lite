# Database Schema

IT Tasker uses **SQLite** with WAL (Write-Ahead Logging) mode for concurrent reads. The database file is created automatically on first run alongside `app.py`.

## Tables

### `walkin_tickets`

Stores walk-in / phone-in / daily IT requests.

| Column | Type | Default | Description |
|---|---|---|---|
| `id` | INTEGER | Auto-increment | Primary key |
| `date` | TEXT | — | Date the issue was reported (`YYYY-MM-DD`) |
| `category` | TEXT | NULL | Issue category (e.g. Hardware, Software) |
| `location` | TEXT | NULL | Location of the user or issue |
| `description` | TEXT | NULL | Description of the issue |
| `reported_by` | TEXT | NULL | Name of the person reporting |
| `additional_info` | TEXT | NULL | Extra notes or follow-up details |
| `assigned_to` | TEXT | NULL | Staff member(s) assigned (comma-separated) |
| `resolved_date` | TEXT | NULL | Date resolved (`YYYY-MM-DD`) |
| `status` | TEXT | `'IN PROGRESS'` | Current status |
| `created_at` | TEXT | `datetime('now')` | Row creation timestamp |
| `updated_at` | TEXT | `datetime('now')` | Last update timestamp |

**Indexes:** `idx_walkin_date` (date), `idx_walkin_status` (status)

### `escalated_tickets`

Stores tickets escalated to an external helpdesk or vendor.

| Column | Type | Default | Description |
|---|---|---|---|
| `id` | INTEGER | Auto-increment | Primary key |
| `date` | TEXT | — | Date the issue was reported |
| `area` | TEXT | NULL | Functional area or department |
| `building` | TEXT | NULL | Building name or number |
| `office` | TEXT | NULL | Office or room identifier |
| `description` | TEXT | NULL | Description of the issue |
| `reported_by` | TEXT | NULL | Name of the person reporting |
| `escalated_by` | TEXT | NULL | Person who raised the external ticket |
| `ticket_number` | TEXT | NULL | External ticket/incident ID |
| `escalation_date` | TEXT | NULL | Date escalated externally |
| `additional_info` | TEXT | NULL | Extra notes |
| `resolved_date` | TEXT | NULL | Date resolved |
| `status` | TEXT | `'IN PROGRESS'` | Current status |
| `created_at` | TEXT | `datetime('now')` | Row creation timestamp |
| `updated_at` | TEXT | `datetime('now')` | Last update timestamp |

**Indexes:** `idx_escalated_date` (date), `idx_escalated_status` (status)

### `users`

Stores application user accounts.

| Column | Type | Default | Description |
|---|---|---|---|
| `id` | INTEGER | Auto-increment | Primary key |
| `username` | TEXT | — | Unique username |
| `password_hash` | TEXT | — | Werkzeug PBKDF2 password hash |
| `created_at` | TEXT | `datetime('now')` | Account creation timestamp |

## Database Location

The database file is stored in the same directory as `app.py`. The filename is controlled by `DATABASE_NAME` in `config.py` (default: `it_tasker.db`).

## Backing Up

Since the database is a single file, you can back it up by simply copying it:

```bash
cp it_tasker.db it_tasker_backup_$(date +%Y%m%d).db
```
