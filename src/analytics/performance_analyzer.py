import pandas as pd
import matplotlib.pyplot as plt

class PerformanceAnalyzer:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def generate_report(self):
        df = pd.read_sql_query("SELECT * FROM accounts", self.db_manager.conn)

        plt.figure(figsize=(10, 6))
        df[['friends_count', 'posts_count', 'comments_count']].plot(kind='bar')
        plt.title('Статистика аккаунтов')
        plt.xlabel('Аккаунты')
        plt.ylabel('Количество')
        plt.legend(['Друзья', 'Посты', 'Комментарии'])
        plt.savefig('performance_report.png')
        plt.close()
