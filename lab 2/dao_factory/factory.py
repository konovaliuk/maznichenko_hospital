from dao import *


class DaoFactory:
    def __init__(self, connection_pool):
        self.pool = connection_pool
        self.dao_imp = {'user': UserDAO(self.pool),
                        'request': RequestDAO(self.pool),
                        'feedback': FeedbackDAO(self.pool),
                        'roles': RoleDAO(self.pool)}

    def get_dao_implementation(self, option: str):
        return self.dao_imp[option]
