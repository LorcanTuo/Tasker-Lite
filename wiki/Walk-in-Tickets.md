# Walk-in Tickets

Walk-in tickets are used to log day-to-day requests from users who walk in, call, or email your IT team.

## Viewing Tickets

Navigate to **Walk-in Tickets** in the sidebar. The list view shows all walk-in tickets in reverse chronological order.

### Filtering

Use the controls at the top of the list to narrow results:

- **Status** — Filter by `IN PROGRESS`, `RESOLVED`, or any custom status
- **Category** — Filter by ticket category (categories are auto-populated from existing data)
- **Search** — Free-text search across description, reported by, and additional info fields

## Creating a Ticket

1. Click **New** on the Walk-in Tickets page (or use the quick-entry button on the Dashboard)
2. Fill in the form fields:

| Field | Required | Description |
|---|---|---|
| **Date** | Yes | Date the issue was reported (defaults to today) |
| **Category** | No | Type of issue (e.g. Hardware, Software, Network) — type a new value or pick from suggestions |
| **Location** | No | Where the user/issue is located |
| **Description** | Yes | Details of the issue |
| **Reported By** | No | Name of the person reporting |
| **Additional Info** | No | Extra notes, follow-up details |
| **Assigned To** | No | Staff member handling the ticket — supports comma-separated names |
| **Resolved Date** | No | Date the issue was resolved |
| **Status** | Yes | Current status (defaults to `IN PROGRESS`) |

3. Click **Save**

## Editing a Ticket

Click the **Edit** button on any ticket row to open the edit form. All fields can be updated.

## Quick Resolve

To quickly mark a ticket as resolved without opening the edit form:

- Click the **Resolve** button on the ticket row (available on both the list page and dashboard)
- The ticket status is set to `RESOLVED` and the resolved date is set to today

## Customisation

The label, icon, and URL prefix for walk-in tickets can be changed in `config.py`. See [[Configuration]] for details.
