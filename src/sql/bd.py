import datetime
import sqlite3
from datetime import datetime


class BotDB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, db_file):
        try:

            self.conn = sqlite3.connect(db_file, timeout=30)
            print('Подключился к SQL DB:', db_file)
            self.cursor = self.conn.cursor()
            self.check_table()
        except Exception as es:
            print(f'Ошибка при работе с SQL {es}')

    def check_table(self):

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                                f"stop_word (id_pk INTEGER PRIMARY KEY AUTOINCREMENT, word TEXT,"
                                f"other TEXT)")

        except Exception as es:
            print(f'SQL исключение check_table stop_word {es}')

    def get_stop_word(self):

        result = self.cursor.execute(f"SELECT * FROM stop_word")

        response = result.fetchall()

        return response

    def add_stop_word(self, word):

        result = self.cursor.execute(f"SELECT * FROM stop_word WHERE word='{word}'")

        response = result.fetchall()

        if response == []:
            self.cursor.execute("INSERT OR IGNORE INTO stop_word ('word') VALUES (?)",
                                (word,))

            self.conn.commit()

            return True

        return False

    def del_word(self, id_pk):

        try:
            result = self.cursor.execute(f"DELETE FROM stop_word WHERE id_pk = '{id_pk}'")

            self.conn.commit()

            x = result.fetchall()

        except Exception as es:
            msg = (f'Ошибка SQL del_word: {es}')
            print(msg)

            return False

        return True

    def close(self):
        # Закрытие соединения
        self.conn.close()
        print('Отключился от SQL BD')
