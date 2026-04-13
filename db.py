import sqlite3

conn = sqlite3.connect("emails.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS emails (
    email TEXT,
    status TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def save_email_status(email, status):
    cursor.execute("INSERT INTO emails (email, status) VALUES (?, ?)", (email, status))
    conn.commit()

def update_status(email, status):
    cursor.execute("UPDATE emails SET status=? WHERE email=?", (status, email))
    conn.commit()