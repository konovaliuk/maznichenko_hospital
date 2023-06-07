from model.models import Feedback
from dao_interface import FeedbackIDAO


class FeedbackDAO(FeedbackIDAO):
    def __init__(self, session):
        self.session = session

    def insert(self, feedback: Feedback):
        self.session.add(feedback)
        self.session.commit()

    def select(self, feedback_id):
        return self.session.query(Feedback).filter(Feedback.id == feedback_id).first()

    def update(self, feedback: Feedback):
        self.session.merge(feedback)
        self.session.commit()

    def update_text(self, feedback_id, text):
        feedback = self.select(feedback_id)
        if feedback:
            feedback.text = text
            self.session.commit()

    def delete(self, feedback_id):
        feedback = self.select(feedback_id)
        if feedback:
            self.session.delete(feedback)
            self.session.commit()

    def read_all(self):
        return self.session.query(Feedback).all()

    def select_request_id(self, doctor_id):
        return self.session.query(Feedback.request_id).filter(Feedback.doctor_id == doctor_id).all()
