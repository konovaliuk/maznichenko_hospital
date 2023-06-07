from abc import ABC, abstractmethod
from model.models import Illness


class IllnessIDAO(ABC):
    @abstractmethod
    def select(self, illness_id: int):
        pass

    @abstractmethod
    def insert(self, illness: Illness):
        pass

    @abstractmethod
    def update(self, illness: Illness):
        pass

    @abstractmethod
    def delete(self, illness_id: int):
        pass