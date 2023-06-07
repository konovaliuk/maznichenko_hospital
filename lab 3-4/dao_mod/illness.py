from model.models import Illness
from dao_interface import IllnessIDAO


class IllnessDAO(IllnessIDAO):
    def __init__(self, session):
        self.session = session

    def insert(self, illness: Illness):
        self.session.add(illness)
        self.session.commit()

    def select(self, illness_id):
        return self.session.query(Illness).filter(Illness.id == illness_id).first()

    def update_all(self, illness: Illness):
        self.session.merge(illness)
        self.session.commit()

    def update_status(self, illness_id, status):
        request = self.select(illness_id)
        if request:
            request.status = status
            self.session.commit()

    def delete(self, illness_id):
        request = self.select(illness_id)
        if request:
            self.session.delete(request)
            self.session.commit()

    def read_all(self):
        return self.session.query(Illness).all()

    def read_by_status(self, status):
        return self.session.query(Illness).filter(Illness.status == status).all()

    def read_by_user_id(self, user_id):
        return self.session.query(Illness).filter(Illness.user_id == user_id).all()

    def read_healed(self, user_id):
        return self.session.query(Illness).filter(Illness.user_id == user_id, Illness.status == 'healed').all()
