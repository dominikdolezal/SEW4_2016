"""
Einfuehrungsbeispiel fuer OOP

"""
from __future__ import print_function
__author__ = 'Walter Rafeiner-Magor'
class Employee(object):
    """ Doc-String der Klasse

        :param str name: Name des Mitarbeiters
        :param float salary: Gehalt des Mitarbeiters
        :ivar str name: Name des Mitarbeiters
        :ivar float salary: Gehalt des Mitarbeiters
    """
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.empCount += 1
    @staticmethod
    def displayCount():
        """
        Gibt die Anzahl der Objekte aus

        :returns: count of objects
        :rtype: None

        """
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        """
        Ausgabe eines Mitarbeiters

        :return: name and salary
        :rtype: None

        """
        print ("Name : ", self.name,  ", Salary: ", self.salary)

if __name__ == '__main__':
# Unser erstes Objekt der Klasse
    emp1 = Employee("Andrea", 2000)
# Das wird unser zweites Objekt
    emp2 = Employee("Franziska", 5000)
# Ausgabe der Mitarbeiter
    emp1.displayEmployee()
    emp2.displayEmployee()
# Ausgabe der Anzahl aller Mitarbeiter
    print ("Total Employee %d" % Employee.empCount)
# Mit Attributen waehrend der Laufzeit arbeiten:
    hasattr(emp1, 'age')    # True, falls das Attribut 'age' existiert
    setattr(emp1, 'age', 8) # Setter fuer das Attribut 'age'
    getattr(emp1, 'age')    # Getter fuer das Attribut 'age'
    delattr(emp1, 'age')    # Das Attribute 'age' wird geloescht!