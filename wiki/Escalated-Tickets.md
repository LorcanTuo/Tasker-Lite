# Escalated Tickets

Escalated tickets track issues that have been raised with an external helpdesk or vendor (e.g. ServiceNow, Jira, Zendesk).

## Viewing Tickets

Navigate to **Escalated Tickets** in the sidebar. The list view shows all escalated tickets in reverse chronological order.

### Filtering

- **Status** — Filter by `IN PROGRESS`, `RESOLVED`, or any custom status
- **Area** — Filter by area (auto-populated from existing data)
- **Search** — Free-text search across description, reported by, ticket number, and additional info

## Creating a Ticket

1. Click **New** on the Escalated Tickets page
2. Fill in the form fields:

| Field | Required | Description |
|---|---|---|
| **Date** | Yes | Date the issue was reported (defaults to today) |
| **Area** | No | Functional area or department |
| **Building** | No | Building name or number |
| **Office** | No | Office or room identifier |
| **Description** | Yes | Details of the issue |
| **Reported By** | No | Name of the person reporting |
| **Escalated By** | No | Person who raised the external ticket |
| **Ticket Number** | No | External ticket/incident ID (e.g. INC00012345) |
| **Escalation Date** | No | Date the issue was escalated externally |
| **Additional Info** | No | Extra notes or follow-up details |
| **Resolved Date** | No | Date the issue was resolved |
| **Status** | Yes | Current status (defaults to `IN PROGRESS`) |

3. Click **Save**

## Editing a Ticket

Click the **Edit** button on any ticket row to update the details.

## Quick Resolve

Click the **Resolve** button on a ticket row to immediately mark it as resolved with today's date.

## Customising Field Labels

The field labels for escalated tickets are fully configurable in `config.py`. This lets you match the terminology of your external ticketing system:

```python
# Example for ServiceNow
ESCALATED_SYSTEM_NAME     = "ServiceNow"
ESCALATED_NUMBER_LABEL    = "INC Number"
ESCALATED_DATE_LABEL      = "ServiceNow Date"
ESCALATED_RAISED_BY_LABEL = "Raised By"
```

See [[Configuration]] for the full list of options.
