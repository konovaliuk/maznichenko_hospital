from model import *
from dao_interface import FeedbackIDAO


class FeedbackDAO(FeedbackIDAO):
    def __init__(self, connection_pool):
        self.connection_object = connection_pool.get_connection()
        self.mycursor = self.connection_object.cursor()

    def write(self, query, vals):
        try:
            self.mycursor.execute(query, vals)
            self.connection_object.commit()
        except Exception as e:
            print(e)
            print('Write error')

    def read(self, query, vals):
        try:
            self.mycursor.execute(query, vals)
            result = self.mycursor.fetchone()
            return result
        except Exception as e:
            print(e)
            print('Read error')

    def insert(self, feedback: Feedback):
        query = "INSERT INTO feedbacks (text, illness_id, doctor_id)" \
                " VALUES (%s, %s, %s)"
        vals = (feedback.text, feedback.illness_id, feedback.doctor_id)
        self.write(query, vals)

    def select(self, feedback_id):
        query = "select * from feedbacks where id=%s"
        vals = (feedback_id,)
        return self.read(query, vals)

    def update(self, feedback: Feedback):
        query = 'UPDATE feedbacks SET text=%s, request_id=%s, master_id=%s WHERE id=%s'
        vals = (feedback.text, feedback.illness_id, feedback.doctor_id, feedback.id)
        self.write(query, vals)

    def delete(self, feedback_id):
        query = 'DELETE FROM feedbacks WHERE id=%s'
        vals = (feedback_id,)
        self.write(query, vals)