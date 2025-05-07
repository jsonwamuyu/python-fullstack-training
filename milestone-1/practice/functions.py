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

def check_number_input(num):
    """
    Return True if number is even number(divisible by 2)

    Parameters:
        num(int, float): The number to be checked

    Returns:
        print
    """

    if num % 2 == 0:
        print('Even number')
    else:
        print("Not even number")


check_number_input(4)
check_number_input(1)

def hello():
    return 'Mike'

n = hello()
print(n)