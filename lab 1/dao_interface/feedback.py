from abc import ABC, abstractmethod
from model import Feedback


class FeedbackIDAO(ABC):
    @abstractmethod
    def select(self, feedback_id: int):
        pass

    @abstractmethod
    def insert(self, feedback: Feedback):
        pass

    @abstractmethod
    def update(self, feedback: Feedback):
        pass

    @abstractmethod
    def delete(self, feedback_id: int):
        pass
