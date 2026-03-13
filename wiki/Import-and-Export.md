# Import and Export

## Importing Tickets from Excel

You can bulk-import tickets from an existing `.xlsx` spreadsheet.

### Steps

1. Navigate to **Import** in the sidebar
2. Click **Choose File** and select your `.xlsx` file
3. Click **Import**

### Expected Spreadsheet Format

The importer looks for sheets matching the configured labels (by default **"Walk-in Tickets"** and **"Escalated Tickets"**). Data rows start at **row 3** (rows 1–2 are assumed to be headers).

#### Walk-in Tickets Sheet

| Column | Field |
|---|---|
| A | Date |
| B | Category |
| C | Location |
| D | Description |
| E | Reported By |
| F | Additional Info |
| G | Assigned To |
| H | Resolved Date |
| I | Status |

#### Escalated Tickets Sheet

| Column | Field |
|---|---|
| A | Date |
| B | Area |
| C | Building |
| D | Office |
| E | Description |
| F | Reported By |
| G | Escalated By |
| H | Ticket Number |
| I | Escalation Date |
| J | Additional Info |
| K | Resolved Date |
| L | Status |

### Notes

- Rows without a date value in column A are skipped
- Date values can be Excel date objects or `YYYY-MM-DD` strings
- Missing status values default to `IN PROGRESS`
- The sheet names must match the labels in `config.py` (e.g. if you changed `WALKIN_LABEL` to `"Daily Tickets"`, the sheet must be named `"Daily Tickets"`)

### Tip

The easiest way to get the correct format is to **export** your existing data first (see below) and use that file as a template.

## Exporting to Excel

### From Reports

1. Navigate to **Reports**
2. Select a date range and generate a report
3. Click **Export to Excel**

This downloads a styled `.xlsx` workbook with three sheets:

- **Status Report** — Summary counts
- **Walk-in Tickets** — All walk-in tickets in the date range
- **Escalated Tickets** — All escalated tickets in the date range

### Export All Data

Generate a report with a very wide date range (e.g. `2000-01-01` to `2099-12-31`) to export everything.
