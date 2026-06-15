import sqlite3


def connect_db():
    conn = sqlite3.connect("tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        job_role TEXT,
        location TEXT,
        salary TEXT,
        applied_date TEXT,
        status TEXT,
        notes TEXT
    )
    """)

    conn.commit()

    return conn, cursor