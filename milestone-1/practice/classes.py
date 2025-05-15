"""
Class variables are defined at class level while instance variables
are defined inside methods using self.

When class variable is changed, it affects all the instances unless overridden by instance variable
self refers to the current instance of the class

"""

class Employee:

    # Class variable - store data that want to be shared across all instances (objects).
    company_name = 'Twitter Inc.'

    def __init__(self, fullname, title, salary):
        # Instance variable - store data that is unique to each object (instance of a class).
        self.fullname = fullname
        self.title = title
        self.salary = salary


    # Instance methods -
    def hello(self):
        return self.fullname


emp1 = Employee('John Doe', 'Manager', 45000)
print(emp1.fullname)

emp2 = Employee('Jane Doe', 'Secretary', 20000)
print(emp2.fullname)

print(emp1.company_name) # Twitter Inc.
print(emp2.company_name) # Twitter Inc.
print(Employee.company_name) # Twitter Inc.



class Book:
    book_count = 0 # Class variable to track how many books created

    def __init__(self, title, author):
        self.title = title
        self.author = author

        # Increase book count whenever a new instance is created.
        Book.book_count+=1

    def book_details(self):
        """Display book info"""

        return f'{self.title} {self.author}'

    @classmethod
    def current_book_count(cls):
        return cls.book_count

    @staticmethod
    def is_valid(st):
        if (len(st) == 10 or len(st) == 13) and st.isdigit():
            return True
        return False

    @classmethod
    def your_age(cls, fullname, birth_year):
        current_year = 2025
        old = current_year - birth_year
        return cls(fullname, old) # Create a new Book instance


kisimani = Book('Kifo Kisimani', "Ken Wali Bora")
print(kisimani.book_details())
book = kisimani.your_age("Mike Mundu", 1994)


class Car:
    WHEELS = 4 # Class variable

    def __init__(self, model, color):
        self.model = model
        self.color = color


    # Modify class variables
    @classmethod
    def change_wheels(cls, new_wheels):
        cls.WHEELS = new_wheels

    """
    Behave like regular functions but live withing class's namespace.
    Can not access or modify class or instance state.
    No special first parameter e.g self or cls.
    Used as helper/utility functions logically related to the class
    Functions that do not need class or instance state
    """

    @staticmethod
    def calculate_discount(price):
        if price > 10000:
            price = 0.95 * price
        return price

print(Car.calculate_discount(20000))
Car.change_wheels(2)
print(Car.WHEELS)


class Temperature:
    """Calculate temperatures in different units."""
    TEMP_UNITS = 'Celsius'

    def __init__(self,temp):
        self.temp = temp

    def display_temp(self):
        """Display current temperatures"""
        if self.TEMP_UNITS == 'Celsius':
            return f'{self.temp}°C'
        elif self.TEMP_UNITS == 'Fahrenheit':
            f_temp = self.c_to_f(self.temp)
            return f'{f_temp}°F'
        else:
            return f'{self.temp} {self.TEMP_UNITS}'

    @classmethod
    def set_temp_units(cls, new_units):
        """Change new units"""
        cls.TEMP_UNITS = new_units

    @staticmethod
    def c_to_f(reading_celsius):
        """Convert temp from Celsius to Far"""
        return (reading_celsius*9/5)+32

joto = Temperature(25)
print('Current temperatures',joto.display_temp())

Temperature.set_temp_units('Fahrenheit')
print('New tem in Fahr: ', joto.display_temp())