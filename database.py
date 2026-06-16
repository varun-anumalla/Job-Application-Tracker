import sqlite3


def get_connection():
    conn = sqlite3.connect("tracker.db")
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        job_role TEXT NOT NULL,
        location TEXT,
        salary TEXT,
        applied_date TEXT,
        status TEXT,
        notes TEXT
    )
    """)

    conn.commit()
    conn.close()