import sqlite3
import time
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "sensor_data.db"

#Open a connection to the SQLite database file. If the file doesn't exist, SQLite will create it
def get_connection():
    return sqlite3.connect(DB_PATH)

#Create our sensor Data table if it dosent exist
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL NOT NULL,
            temperature REAL NOT NULL,
            voltage REAL NOT NULL,
            state INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

#inserts our data into the table
def log_reading(temperature: float, voltage: float, state: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO sensor_data (timestamp, temperature, voltage, state)
        VALUES (?, ?, ?, ?)
        """,
        (time.time(), float(temperature), float(voltage), int(state)),
    )
    conn.commit()
    conn.close()

#return n rows from the table as tuples
def get_history(limit: int = 20):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT timestamp, temperature, voltage, state
        FROM sensor_data
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    )
    rows = cur.fetchall()
    conn.close()
    return rows

