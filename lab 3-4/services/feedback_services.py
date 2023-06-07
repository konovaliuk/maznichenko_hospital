from connection import get_session
from dao_factory import factory
from model.models import Feedback


class FeedbackServices:
    session = get_session()
    dao_factory = factory.DaoFactory(session)
    feedback_dao = dao_factory.get_dao_implementation('feedback')

    def take_feedback(self, feedback: Feedback):
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

    def get_requests_id(self, doctor_id):
        try:
            self.feedback_dao.select_request_id(doctor_id)
        except:
            return False
