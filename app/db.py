import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Optional, Iterable

DB_PATH = Path(__file__).resolve().parent.parent / "data.sqlite3"

SCHEMA = """
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS users (
    tg_user_id INTEGER PRIMARY KEY,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    market TEXT NOT NULL,
    market_item_id TEXT NOT NULL,
    name TEXT NOT NULL,
    weapon TEXT,
    skin TEXT,
    wear TEXT,
    phase TEXT,
    url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_user_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    target_price REAL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(tg_user_id) REFERENCES users(tg_user_id) ON DELETE CASCADE,
    FOREIGN KEY(item_id) REFERENCES items(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER NOT NULL,
    source TEXT NOT NULL,
    price REAL NOT NULL,
    currency TEXT NOT NULL,
    ts TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(item_id) REFERENCES items(id) ON DELETE CASCADE
);
"""


@contextmanager
def conn():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    try:
        yield con
    finally:
        con.close()


with conn() as c:
    c.executescript(SCHEMA)
    c.commit()


# CRUD helpers

def ensure_user(tg_user_id: int):
    with conn() as c:
        c.execute("INSERT OR IGNORE INTO users(tg_user_id) VALUES (?)", (tg_user_id,))
        c.commit()


def upsert_item(market: str, market_item_id: str, name: str, url: str,
                weapon: Optional[str] = None, skin: Optional[str] = None,
                wear: Optional[str] = None, phase: Optional[str] = None) -> int:
    with conn() as c:
        cur = c.execute(
            """
            SELECT id FROM items WHERE market=? AND market_item_id=?
            """,
            (market, market_item_id),
        )
        row = cur.fetchone()
        if row:
            return row[0]
        cur = c.execute(
            """
            INSERT INTO items(market, market_item_id, name, weapon, skin, wear, phase, url)
            VALUES(?,?,?,?,?,?,?,?)
            """,
            (market, market_item_id, name, weapon, skin, wear, phase, url),
        )
        c.commit()
        return cur.lastrowid


def add_user_item(tg_user_id: int, item_id: int, target_price: Optional[float] = None):
    with conn() as c:
        c.execute("INSERT INTO user_items(tg_user_id, item_id, target_price) VALUES (?,?,?)",
                  (tg_user_id, item_id, target_price))
        c.commit()


def list_user_items(tg_user_id: int) -> Iterable[tuple]:
    with conn() as c:
        cur = c.execute(
            """
            SELECT ui.id, i.id, i.name, i.url
            FROM user_items ui
            JOIN items i ON i.id = ui.item_id
            WHERE ui.tg_user_id=?
            ORDER BY ui.id DESC
            """,
            (tg_user_id,)
        )
        return cur.fetchall()
