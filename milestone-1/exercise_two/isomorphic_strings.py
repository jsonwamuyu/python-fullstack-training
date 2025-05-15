"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""

def is_isomorphic(s: str, t: str) -> bool:
    # Check if both string length is equal
    if len(s) == len(t):

        return True
    return False

print(is_isomorphic('hello', 'hebbo'))