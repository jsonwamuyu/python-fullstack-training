"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


def is_isomorphic(s: str, t: str) -> bool:
    """
    Map each string in separate dictionaries and store each unique
    character as key and its count as value.Then compare the two dictionaries
    """
    s_mapping = {}  # Holds s mappings.
    t_mapping = {}  # Holds t mappings.
    s_count = 0
    t_count = 0

    if len(s) == len(t):
        # Map through s and update count for each unique character found.
        for i_s, s_value in enumerate(s):
            if s_value in s_mapping:
                s_count += 1
            else:
                s_count = 1
            s_mapping[s_value] = s_count

        # Map through t and update count for each unique character found.
        for i_t, t_value in enumerate(t):
            if t_value in t_mapping:
                t_count += 1
            else:
                t_count = 1
            t_mapping[t_value] = t_count

        # Check if the two dictionaries are equal
        print(s_mapping)
        print(t_mapping)
        if len(s_mapping) is len(t_mapping):
            return True

    return False


s1 = "alil"
t1 = "aooy"
print(is_isomorphic(s1, t1))
