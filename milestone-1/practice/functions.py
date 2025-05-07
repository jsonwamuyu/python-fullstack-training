"""
Function Design Process

1. What task do I want this functon to do?
    e.g I want this function to calculate the area of a triangle
2. What DATA(INPUTS) does this function needs to do this tasks?
    Example: length and width → def area(length, width)
3. What should it return (if anything)?
    should it give back a result or just perform an action
    example: return length*width
4. How will you name it?
    Use clear, descriptive names. Should indicate what the function does
"""

# We’ll write a function to check whether a number is a prime number.


def check_number_is_prime(num):
    """
    Check whether a number is prime.
    A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

    :param num: Number to be checked

    :return: Boolean(True is prime, False otherwise)
    """
    if num < 2:
        return False
    # for i in range(2, num - 1):
    for i in range(2, int(num ** 0.5 ) + 1):
        if num % i == 0:
            return False

    return True


print('Test whether 3 is prime: ', check_number_is_prime(3))
print('Test whether 8 is prime: ', check_number_is_prime(8))


def check_number_input(num):
    """
    Return True if number is even number(divisible by 2), False otherwise

    Parameters:
        num(int, float): The number to be checked

    Returns:
        Boolean: True if even, False otherwise
    """

    return num % 2 == 0


print(check_number_input(4))
print(check_number_input(1))


def hello():
    """Greet Mike."""
    return "Mike"


print(hello())
