__author__ = 'uhs374h'
from abc import abstractmethod, ABCMeta


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        """ Updates itself

        :return: Nothing
        """
        pass
