import sqlite3
from pathlib import Path

# Verwaltung der Verbindung zur Datenbank

DB_PATH = Path("data/library.db")

# Öffnen der Datenbankverbindung
def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)  # Ordner 'data/' anlegen, falls nötig
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

# Tabelle mit den books erstellen wenn noch nicht vorhanden
def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER
            );
        """)
    print(f"Database initialized at {DB_PATH.resolve()}")
