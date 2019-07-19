"""
Implement kmp algorithm for pattern matching
Given a pattern and a string check if pattern exists in the string
"""

def KMPSearch(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*pattern_length
    j = 0 # index for pattern[]

    # Preprocess the pattern (Calculate lps[] array)
    computeLPSArray(pattern, pattern_length, lps)

    i = 0 # index for text pattern

    while i < text_length:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == pattern_length:
            print("Found pattern at index " + str(i - j))
            j = lps[j-1]

        # mismatch after j matches
        elif i < text_length and pattern[j] != text[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def computeLPSArray(pattern, pattern_length, lps):
    len = 0 # length of the previous longest prefix suffix

    lps[0]
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < pattern_length:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

txt = "ABCD"
pat = "BC"
KMPSearch(pat, txt)