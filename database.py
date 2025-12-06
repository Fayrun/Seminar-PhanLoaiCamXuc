import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "sentiment.db")

class Database:
    def __init__(self, db_path=DB_PATH):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS sentiment_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            confidence REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def save_result(self, text, sentiment, confidence):
        query = """INSERT INTO sentiment_history (text, sentiment, confidence) VALUES (?, ?, ?)"""
        self.cursor.execute(query, (text, sentiment, confidence))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_history(self, limit=10):
        query = """SELECT id, text, sentiment, confidence, timestamp FROM sentiment_history ORDER BY timestamp DESC LIMIT ?"""
        return self.cursor.execute(query, (limit,)).fetchall()
