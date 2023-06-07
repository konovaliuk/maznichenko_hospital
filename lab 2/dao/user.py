import hashlib
from model import *
from dao_interface import UserIDAO


class UserDAO(UserIDAO):
    def __init__(self, connection_pool):
        self.connection_object = connection_pool.get_connection()
        self.mycursor = self.connection_object.cursor()

    def write(self, query, vals):
        self.mycursor.execute(query, vals)
        self.connection_object.commit()
        return self.mycursor.lastrowid

    def read(self, query, vals):
        self.mycursor.execute(query, vals)
        result = self.mycursor.fetchone()
        return result

    @staticmethod
    def hash(password: str):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def insert(self, user: User):
        query = "INSERT INTO users (login, password, role_id)" \
                " VALUES (%s, %s, %s)"
        vals = (user.login, user.password, user.role)
        self.write(query, vals)

    def select(self, user_id):
        query = "select * from users where id=%s"
        vals = (user_id,)
        return self.read(query, vals)

    def sign_in(self, user: User):
        query = "select * from users where login=%s and password=%s"
        vals = (user.login, user.password)
        return self.read(query, vals)

    def select_login(self, login):
        query = "select * from users where login=%s"
        vals = (login,)
        return self.read(query, vals)

    def update(self, user: User):
        query = 'UPDATE users SET login=%s, password=%s, role_id=%s  WHERE id=%s'
        vals = (user.login, self.hash(user.password), user.role, user.id)
        self.write(query, vals)

    def delete(self, user_id):
        query = 'DELETE FROM users WHERE id=%s'
        vals = (user_id,)
        self.write(query, vals)

    def read_all(self):
        query = "select * from users"
        self.mycursor.execute(query, ())
        return self.mycursor.fetchall()
