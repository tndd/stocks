from abc import ABC, abstractmethod


class AbstractDatabaseSession(ABC):

    @abstractmethod
    def get(self, model_class, id):
        pass

    @abstractmethod
    def add(self, instance):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass
    