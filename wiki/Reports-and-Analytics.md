# Reports and Analytics

IT Tasker provides two types of reporting: built-in HTML/Excel reports and optional R-generated analytics charts.

## Summary Reports

1. Navigate to **Reports** in the sidebar
2. Select a **Start Date** and **End Date**
3. Click **Generate Report**

The report shows:

- **Walk-in Tickets** — Total raised, resolved, and in progress for the period
- **Escalated Tickets** — Total raised, resolved, and in progress for the period
- **Category Breakdown** — Walk-in tickets grouped by category with counts
- **Ticket Details** — Full list of walk-in and escalated tickets in the date range

## Excel Export

From the report view, click **Export to Excel** to download a styled `.xlsx` workbook containing:

| Sheet | Contents |
|---|---|
| **Status Report** | Summary table with raised/completed/in-progress counts per category |
| **Walk-in Tickets** | Full list of walk-in tickets for the date range |
| **Escalated Tickets** | Full list of escalated tickets for the date range |

The Excel file includes formatted headers, auto-sized columns, and borders.

## R Analytics Charts (Optional)

If R and ggplot2 are installed, you can generate visual analytics charts.

### Prerequisites

- **R** must be installed and `Rscript` must be in your system PATH
- The `ggplot2` and `scales` R packages must be installed:
  ```bash
  Rscript -e 'install.packages(c("ggplot2", "scales"))'
  ```

### Generating Charts

1. Navigate to **Reports** in the sidebar
2. Select a date range
3. Click **R Analytics Report**

### Available Charts

| Chart | Description |
|---|---|
| **Tickets by Category** | Horizontal bar chart of walk-in tickets grouped by category |
| **Tickets Over Time** | Line chart showing walk-in ticket volume by date |
| **Status Breakdown** | Bar chart comparing in-progress vs resolved tickets |
| **Escalated by Area** | Horizontal bar chart of escalated tickets grouped by area |

Charts are generated as PNG images and displayed in the browser. They are created in a temporary directory and are not persisted.

### Troubleshooting R Reports

If you see the error _"R is not installed or Rscript is not in PATH"_:

- Verify R is installed: `Rscript --version`
- On macOS, install via Homebrew: `brew install r`
- On Ubuntu/Debian: `sudo apt install r-base`
