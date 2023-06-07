from connection import get_pool
from dao_factory import factory
from model import *


class FeedbackServices:
    pool = get_pool()
    dao_factory = factory.DaoFactory(pool)
    feedback_dao = dao_factory.get_dao_implementation('feedback')

    def take_request(self, feedback: Feedback):
        try:
            return self.feedback_dao.insert(feedback)
        except:
            return False

    def add_feedback(self, feed_id, text):
        try:
            self.feedback_dao.update_text(feed_id, text)
        except:
            return False
        return True

    def get_requests_id(self, master_id):
        try:
            self.feedback_dao.select_request_id(master_id)
        except:
            return False
