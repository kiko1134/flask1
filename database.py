import sqlite3

DB_NAME = 'example.db'

conn = sqlite3.connect(DB_NAME)


conn.cursor().execute('''
    CREATE TABLE IF NOT EXISTS posts 
    (
        post_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        author TEXT, 
        content TEXT
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS comments
    (
        comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER,
        message TEXT,
        FOREIGN KEY(post_id) REFERENCES posts(id)
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

conn.commit()


class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()