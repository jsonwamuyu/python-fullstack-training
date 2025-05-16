def is_valid(s: str) -> bool:
    """
    Valid Parentheses

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    :param s: string

    :return : Boolean - True if valid, False otherwise
    """

    stack = []
    pairs = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in pairs:
            stack.append(pairs[char])  # Push expected closing
        else:
            if not stack or stack.pop() != char:
                return False
    return not stack


print(is_valid("{}"))  # True
print(is_valid('(}}()')) # False
