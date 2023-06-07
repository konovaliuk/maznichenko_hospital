from abc import ABC, abstractmethod


class RoleIDAO(ABC):
    @abstractmethod
    def select(self, role_id: int):
        pass

    @abstractmethod
    def insert(self, role_name):
        pass

    @abstractmethod
    def update(self, role_name, role_id):
        pass

    @abstractmethod
    def delete(self, role_id: int):
        pass
