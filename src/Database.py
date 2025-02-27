import sqlite3


class Context:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("data.db", check_same_thread=False)

    def get_all_users(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM users"

        cursor.execute(query)
        return cursor.fetchall()

    def create_new_user(self, id, name, email, phone, last_name=None):
        cursor = self.connection.cursor()
        query = """INSERT INTO users (id, name, last_name, email, phone)
                VALUES (?, ?, ?, ?, ?)"""

        cursor.execute(query, (id, name, last_name, email, phone))
        self.connection.commit()

    def delete_user(self, id: int):
        cursor = self.connection.cursor()
        query = "DELETE FROM users WHERE id = ?"

        cursor.execute(query, (id,))
        self.connection.commit()

    def update_user(self, id, name, email, phone, last_name=None):
        cursor = self.connection.cursor()
        query = """UPDATE users SET name = ?, last_name = ?, email = ?, phone = ?
                WHERE id = ?"""

        cursor.execute(query, (name, last_name, email, phone, id))
        self.connection.commit()
