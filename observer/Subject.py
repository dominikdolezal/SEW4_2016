__author__ = 'uhs374h'
from abc import abstractmethod, ABCMeta


class Subject(metaclass=ABCMeta):
    def __init__(self):
        """ Initializes the list of observers
        """
        self.observers = []

    def register(self, observer):
        """ Adds the observer to the list of observres

        :param observer: the observer to be added to the list
        :return: None
        """
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        """ Removes the observer from the list if present.
        :param observer: the observer to unregister
        :return: None
        """
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self):
        """ Updates all observers
        :return: None
        """
        for o in self.observers:
            o.update()

    @abstractmethod
    def getState(self):
        """ Gets the observable state

        :return: the observable state
        """
        pass