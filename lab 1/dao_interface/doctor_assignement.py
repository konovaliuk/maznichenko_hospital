from abc import ABC, abstractmethod


class DoctorAssignementIDAO(ABC):
    @abstractmethod
    def select(self, work_id: int):
        pass

    @abstractmethod
    def insert(self, user_id, request_id):
        pass

    @abstractmethod
    def update(self, user_id, request_id):
        pass

    @abstractmethod
    def delete(self, work_id: int):
        pass
