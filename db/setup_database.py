import sqlite3
from .db_conf import db_path, table_name

def create_database():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        titles TEXT NOT NULL,
        content TEXT NOT NULL,
        status TEXT NOT NULL,
        created_date TEXT NOT NULL,
        issue_date TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()