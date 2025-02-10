import sqlite3
import os

def initialize_database():
    # Указываем путь к базе данных
    db_path = os.getenv("DB_PATH", "vk_automation.db")

    # Проверяем, существует ли база данных
    if os.path.exists(db_path):
        print(f"База данных уже существует: {db_path}")
        return

    # Создаем подключение к базе данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создаем таблицы
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT NOT NULL UNIQUE,
            personality TEXT NOT NULL,
            friends_count INTEGER DEFAULT 0,
            posts_count INTEGER DEFAULT 0,
            comments_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            action_type TEXT NOT NULL,
            action_details TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(account_id) REFERENCES accounts(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            metric_name TEXT NOT NULL,
            metric_value REAL NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(account_id) REFERENCES accounts(id)
        )
    ''')

    # Сохраняем изменения
    conn.commit()

    # Закрываем подключение
    conn.close()

    print(f"База данных успешно инициализирована: {db_path}")

if __name__ == "__main__":
    initialize_database()
