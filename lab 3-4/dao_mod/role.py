from dao_interface import RoleIDAO
from model.models import Role


class RoleDAO(RoleIDAO):
    def __init__(self, session):
        self.session = session

    def insert(self, role_name):
        role = Role(name=role_name)
        self.session.add(role)
        self.session.commit()

    def select(self, role_id):
        return self.session.query(Role).filter(Role.id == role_id).first()

    def update(self, role_name, role_id):
        role = self.select(role_id)
        if role:
            role.name = role_name
            self.session.commit()

    def delete(self, role_id):
        role = self.select(role_id)
        if role:
            self.session.delete(role)
            self.session.commit()
