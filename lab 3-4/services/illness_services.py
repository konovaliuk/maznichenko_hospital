from connection import get_session
from dao_factory import factory
from model.models import Illness


class IllnessServices:
    session = get_session()
    dao_factory = factory.DaoFactory(session)
    illness_dao = dao_factory.get_dao_implementation('request')

    def add_illness(self, illness: Illness):
        try:
            self.illness_dao.insert(illness)
            return True
        except:
            return False

    def update_status(self, illness_id, status):
        try:
            self.illness_dao.update_status(illness_id, status)
            return True
        except:
            return False

    def show_by_status(self, status):
        try:
            return self.illness_dao.read_by_status(status)
        except:
            return False

    def get_by_user_id(self, id):
        try:
            return self.illness_dao.read_by_user_id(id)
        except:
            return False

    def get_by_id(self, id):
        try:
            return self.illness_dao.select(id)
        except:
            return False

    def illness_to_feedback(self, user_id):
        try:
            return self.illness_dao.read_completed
        except:
            return False
