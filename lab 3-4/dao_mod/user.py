import hashlib
from model.models import User
from dao_interface import UserIDAO


class UserDAO(UserIDAO):
    def __init__(self, session):
        self.session = session

    @staticmethod
    def hash(password: str):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def insert(self, user: User):
        user.password = self.hash(user.password)
        self.session.add(user)
        self.session.commit()

    def select(self, user_id):
        return self.session.query(User).filter(User.id == user_id).first()

    def sign_in(self, user: User):
        hashed_password = self.hash(user.password)
        return self.session.query(User).filter(User.login == user.login, User.password == hashed_password).first()

    def select_login(self, login):
        return self.session.query(User).filter(User.login == login).first()

    def update(self, user: User):
        existing_user = self.select(user.id)
        if existing_user:
            existing_user.login = user.login
            existing_user.password = self.hash(user.password)
            existing_user.role = user.role
            self.session.commit()

    def delete(self, user_id):
        user = self.select(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()

    def read_all(self):
        return self.session.query(User).all()
