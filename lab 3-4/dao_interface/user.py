from abc import ABC, abstractmethod
from model.models import User


class UserIDAO(ABC):
    @abstractmethod
    def select(self, user_id: int):
        '''
        Should return user with given id
        or None if no such user found
        '''

    @abstractmethod
    def insert(self, user: User):
        '''
        Should insert given user
        '''

    @abstractmethod
    def update(self, user: User):
        '''
        Should update given user
        '''

    @abstractmethod
    def delete(self, user_id: int):
        '''
        Should delete given user by id
        '''