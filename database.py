# database.py
import sqlite3

def log_interaction(user_input, bot_reply):
    conn = sqlite3.connect("chatlog.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_reply TEXT
        )
    """)
    cursor.execute("INSERT INTO logs (user_input, bot_reply) VALUES (?, ?)", (user_input, bot_reply))
    conn.commit()
    conn.close()
