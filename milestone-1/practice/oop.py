"""
A class is a blueprint for creating an object. It is a collection of
attributes and methods.


"""

class Person:
    """A class to represent a person."""

    species = 'mamalia'

    def __init__(self, name, gender):
        self.name = name
        self.gender =gender

    def person_details(self):
        """Return person name and age."""

        return f'Name: {self.name}, gender: {self.gender}'