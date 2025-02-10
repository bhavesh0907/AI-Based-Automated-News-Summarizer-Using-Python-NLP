import sqlite3

def save_summary(url, summary):
    conn = sqlite3.connect("news_summaries.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS summaries (url TEXT, summary TEXT)")
    cursor.execute("INSERT INTO summaries (url, summary) VALUES (?, ?)", (url, summary))
    conn.commit()
    conn.close()

def fetch_summaries():
    conn = sqlite3.connect("news_summaries.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM summaries")
    data = cursor.fetchall()
    conn.close()
    return data
