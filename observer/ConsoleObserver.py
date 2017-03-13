from observer.Observer import Observer


class ConsoleObserver(Observer):
    def __init__(self, name, subject):
        """
        Creates a simple observer which prints to the console.
        :param name: the name of this observer
        :param subject: the subject to observe
        """
        self.name = name
        self.subject = subject
        subject.register(self)

    def update(self):
        """

        :return:
        """
        self.printOutput(self.subject.getState())

    def printOutput(self, value):
        print("ConsoleObserver %s: %f" % (self.name, value))
