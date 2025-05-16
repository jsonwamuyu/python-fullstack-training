"""
Inheritance

Allows you to create new classes (child/subclasses) that inherit attribute
and methods from an existing class (parent/super class)

"""


class Parent:
    def greet(self):
        print("Hello from parents")


class Child(Parent):
    # Override greet method in parent.
    def greet(self):
        super().greet()  # Call parent greet method
        print("Greet from child")


parent = Parent()
parent.greet()

child = Child()
child.greet()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal sound.")


class Dog(Animal):
    # Override speak method from parent
    def speak(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} is fetching.")


class Cat(Animal):
    def speak(self):
        print("Meow")

    def scratch(self):
        print(f"{self.name} is scratching.")


animal = Animal("Janta")
animal.speak()

bale = Dog("Bale")
bale.fetch()
bale.speak()

kihunyu = Cat("Kihunyu")
kihunyu.scratch()
kihunyu.speak()


# UNIVERSITY EXAMPLE
class Person:
    """Base class - store name and id"""

    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def get_person_details(self):
        return f"NAME: {self.name} ID: {self.person_id}"


class Employee(Person):
    """Inherit from Person and add position."""

    def __init__(self, name, person_id, position):
        super().__init__(name, person_id)  # Call parent (Person) constructor
        self.position = position

    def get_position(self):
        return f"POSITION: {self.position}"


class Athlete:
    """Stores sport for a person."""

    def __init__(self, sport):
        self.sport = sport

    def get_sport(self):
        return f"SPORT: {self.sport}"


class Student(Employee, Athlete):
    """Inherits from Employee and Athlete - add grade"""

    def __init__(self, name, person_id, position, sport, grade):
        super().__init__(name, person_id, position
        )  # Initialize Employee (and Person).
        super().__init__(sport)  # Initialize Athlete.
        self.grade = grade

    def get_grade(self):
        return f"GRADE: {self.grade}"

    def get_info(self):
        return (
            f"NAME: {self.name} ID: {self.person_id} POSITION: {self.position} "
            f"SPORT: {self.sport} GRADE: {self.grade}"
        )


class GraduateStudent(Student):
    """Inherit from Student, add thesis and override get_info to include it."""

    def __init__(self, name, person_id, position, sport, grade, thesis):
        super().__init__(name, person_id, position, sport, grade)
        self.thesis = thesis

    def get_info(self):
        return (
            f"NAME: {self.name} ID: {self.person_id} POSITION: {self.position} "
            f"SPORT: {self.sport} GRADE: {self.grade} THESIS: {self.thesis}"
        )


# Initialize a student
student = Student("John Sue", 435555, "Inter", "soccer", "A")

print(student.get_person_details())
print(student.get_position())
print(student.get_sport())
print(student.get_grade())
print(student.get_info())

graduate = GraduateStudent(
    "Richard", 34344, "Attache", "Baseball", "A", "Life in Prison"
)
print(graduate.get_info())


print(Student.__mro__)
