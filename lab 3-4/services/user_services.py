from connection import get_session
from dao_factory import factory
from model.models import User
import hashlib


class UserServices:
    session = get_session()
    dao_factory = factory.DaoFactory(session)
    user_dao = dao_factory.get_dao_implementation('user')

    @staticmethod
    def hash(password: str):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def get_user(self, user_id):
        try:
            return User(*self.user_dao.select(user_id))
        except:
            print('invalid id')
            return False

    def register(self, user: User):
        if self.user_dao.select_login(user.login):
            return False  # user already exists
        if user.password == '':
            return False  # empty password
        user.password = self.hash(user.password)
        try:
            id = self.user_dao.insert(user)
            user.id = id
            return user
        except:
            print('Database error')
            return False

    def sign_in(self, user: User):
        user.password = self.hash(user.password)
        result = self.user_dao.sign_in(user)
        if result:
            return User(*result)
        else:
            return False  # wrong login or password

    def get_no_feedback(self, id):
        pass
