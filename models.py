import sqlite3
import os
from datetime import datetime
from werkzeug.security import generate_password_hash

def _db_path():
    from config import DATABASE_NAME
    base_dir = os.environ.get('DATABASE_PATH',
                              os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, DATABASE_NAME)

def get_db():
    conn = sqlite3.connect(_db_path())
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

def init_db():
    conn = get_db()
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS walkin_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT,
            location TEXT,
            description TEXT,
            reported_by TEXT,
            additional_info TEXT,
            assigned_to TEXT,
            resolved_date TEXT,
            status TEXT NOT NULL DEFAULT 'IN PROGRESS',
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS escalated_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            area TEXT,
            building TEXT,
            office TEXT,
            description TEXT,
            reported_by TEXT,
            escalated_by TEXT,
            ticket_number TEXT,
            escalation_date TEXT,
            additional_info TEXT,
            resolved_date TEXT,
            status TEXT NOT NULL DEFAULT 'IN PROGRESS',
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now'))
        );

        CREATE INDEX IF NOT EXISTS idx_walkin_date ON walkin_tickets(date);
        CREATE INDEX IF NOT EXISTS idx_walkin_status ON walkin_tickets(status);
        CREATE INDEX IF NOT EXISTS idx_escalated_date ON escalated_tickets(date);
        CREATE INDEX IF NOT EXISTS idx_escalated_status ON escalated_tickets(status);

        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
    ''')
    conn.commit()

    # Seed a default admin user if no users exist
    count = conn.execute("SELECT COUNT(*) as c FROM users").fetchone()['c']
    if count == 0:
        conn.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            ('admin', generate_password_hash('admin123'))
        )
        conn.commit()

    conn.close()
