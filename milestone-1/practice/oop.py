"""
A class is a blueprint for creating an object. It is a collection of
attributes and methods.

"""


class Person:
    """A class to represent a person."""

    species = "mamalia"

    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet_person(self):
        """Greet person with their name"""
        print(f"Hello {self.name}")

    def person_details(self):
        """Return person name and age."""

        return f"Name: {self.name}, age: {self.age}"


# Creating object - instance of a class.
mike = Person("Mike", 34)
jane = Person('Jane', 23)
mike.greet_person()
jane.greet_person()
print(mike.person_details())


# Inheritance
class Employee(Person):
    """Inherit from Person class."""

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def employee_details(self):
        return f'Name: {self.name} Age:{self.age} EmployeeId: {self.employee_id}'
