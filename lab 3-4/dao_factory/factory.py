from dao_mod import *


class DaoFactory:
    def __init__(self, session):
        self.session = session
        self.dao_imp = {'user': UserDAO(self.session),
                        'request': IllnessDAO(self.session),
                        'feedback': FeedbackDAO(self.session),
                        'roles': RoleDAO(self.session)}

    def get_dao_implementation(self, option: str):
        return self.dao_imp[option]
