import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (id) VALUES ( ?)",
                                       (user_id,))

    def all_users(self):
        with self.connection:
            range = self.cursor.execute('SELECT id FROM users').fetchall()
            return len(range)

    def id_users(self):
        with self.connection:
            users = self.cursor.execute('SELECT id FROM users').fetchall()
            return users

    def proverka_number(self, number):
        with self.connection:
            number = self.cursor.execute('SELECT * FROM users WHERE number_film = ?', (number,)).fetchall()
            return bool(len(number))

    def add_film(self, number, film):
        with self.connection:
            number = self.cursor.execute('INSERT INTO users (number_film, film) VALUES (?, ?)', (number, film,))

    def searche_film(self, number):
        with self.connection:
            result = self.cursor.execute('SELECT film FROM users WHERE number_film =? ', (number,)).fetchall()
            return result[0][0]
