"""
Implement naive approach for pattern matching
Given a pattern and a string check if pattern exists in the string
"""


# return indexes at which pattern is present in string
def search(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)

    # loop to slide pattern one by one
    for i in range(text_length - pattern_length + 1):
        j = 0

        # for index i check if next set of characters
        # contain the pattern
        for j in range(0, pattern_length):
            if text[i+j] != pattern[j]:
                break
            if j == pattern_length - 1:
                print("Pattern found at index", i)


txt = "AABAACAADAABAAABAA"
pat = "AABA"
search(pat, txt)