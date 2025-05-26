# scripts/setup_db.py

import sqlite3
from pathlib import Path

def setup_database():
    schema_path = Path(__file__).parent.parent / "lib" / "db" / "schema.sql"
    db_path = Path(__file__).parent.parent / "lib" / "db" / "database.db"

    with sqlite3.connect(db_path) as conn:
        with open(schema_path) as f:
            conn.executescript(f.read())
        print("✅ Database schema has been set up.")

if __name__ == "__main__":
    setup_database()
