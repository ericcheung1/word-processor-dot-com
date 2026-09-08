import sqlite3
from pathlib import Path

DB_DIR = Path("app/data/cache.db")

def init_sqlite():
    """Initialized sqlite and creates table"""

    DB_DIR = Path("app/data/cache.db")
    DB_DIR.touch(exist_ok=True)
    con = sqlite3.connect(DB_DIR)

    with con:
        con.execute("PRAGMA journal_mode = WAL")

        con.execute("""
        CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
            )
        """)
        con.commit()

    return con


def connect_sqlite():

    DB_DIR.touch(exist_ok=True)
    con = sqlite3.connect(DB_DIR)

    return con


def close_sqlite(con):
    """Closes sqlite connection"""
    con.close()


def query_table():
    """Queries table for post, returns if exists"""
    pass


def write_to_table():
    pass