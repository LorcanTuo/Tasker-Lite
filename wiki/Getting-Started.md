# Getting Started

## Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **R** + `ggplot2` *(optional, only needed for analytics charts)*

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/it-tasker.git
cd it-tasker
```

### 2. Install Python dependencies

```bash
pip install flask flask-login werkzeug openpyxl
```

### 3. (Optional) Install R for analytics charts

**macOS:**
```bash
brew install r
Rscript -e 'install.packages(c("ggplot2", "scales"))'
```

**Ubuntu/Debian:**
```bash
sudo apt install r-base
Rscript -e 'install.packages(c("ggplot2", "scales"))'
```

### 4. Run the application

```bash
python app.py
```

The server starts at **http://127.0.0.1:5001** by default.

## First Login

The default credentials are:

| Username | Password |
|---|---|
| `admin` | `admin123` |

> **⚠️ Change the default password immediately** by navigating to **Change Password** in the sidebar after logging in.

## Post-Install Checklist

1. Change the default admin password
2. Update `SECRET_KEY` in `config.py` to a random string
3. Customise branding and labels in `config.py` (see [[Configuration]])
4. Add additional users via the [[User Management]] page
5. (Optional) Import existing ticket data via [[Import and Export]]

## Project Structure

```
├── app.py           # Flask routes and business logic
├── config.py        # All configurable settings
├── models.py        # SQLite schema and database helpers
├── report.R         # Optional R analytics chart generator
├── templates/       # Jinja2 HTML templates (Bootstrap 5)
│   ├── base.html
│   ├── dashboard.html
│   ├── walkin_form.html
│   ├── walkin_list.html
│   ├── escalated_form.html
│   ├── escalated_list.html
│   ├── reports.html
│   ├── report_view.html
│   ├── r_report.html
│   ├── import.html
│   ├── users.html
│   ├── login.html
│   └── change_password.html
└── README.md
```

## Stopping the Server

Press `Ctrl + C` in the terminal where the server is running.
