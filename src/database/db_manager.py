import sqlite3

class DBManager:
    def __init__(self, db_path="vk_automation.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                phone TEXT UNIQUE,
                personality TEXT,
                friends_count INTEGER DEFAULT 0,
                posts_count INTEGER DEFAULT 0,
                comments_count INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_account(self, phone, personality):
        self.cursor.execute('INSERT INTO accounts (phone, personality, friends_count, posts_count, comments_count) VALUES (?, ?, 0, 0, 0)', (phone, str(personality)))
        self.conn.commit()
