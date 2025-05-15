"""
Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

def word_break(s: str, word_dict: list[str]) -> bool:
    """
    Return true if s can be segmented into a space-separated sequence
    of one or more dictionary words.
    """

    return True

print(word_break('hello', ['He', 'llo'])) # True
print(word_break('hello',['hel','o'])) # False