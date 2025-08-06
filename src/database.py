import sqlite3
import utils

def create_db():
    conn = sqlite3.connect("mappings.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mappings (id INTEGER PRIMARY KEY AUTOINCREMENT, short_url TEXT, long_url TEXT)")

def add_record(long_url):
    short_url = utils.encode()
    with sqlite3.connect("mappings.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mappings (short_url,long_url) values (?,?)",(short_url,long_url))
    return short_url

def get_records(short_url="",long_url=""):
    with sqlite3.connect("mappings.db") as conn:
        cursor = conn.cursor()
        if short_url:
            cursor.execute("SELECT long_url from mappings where short_url=?",[short_url])
            return cursor.fetchall()
        if long_url:
            cursor.execute("SELECT short_url from mappings where long_url=?",[long_url])
            return cursor.fetchall()
        return []

def get_all_records():
    with sqlite3.connect("mappings.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT short_url from mappings")
        result = cursor.fetchall()
        return result

def get_last_id():
    with sqlite3.connect("mappings.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id from mappings order by id desc limit 1;")
        result = cursor.fetchone()
        return result[0] if result else 0