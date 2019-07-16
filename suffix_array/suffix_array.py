"""
Implement suffix array
Given a string generate its suffix array
"""


# return suffix array
def suffix_array_alternative_naive(s):
    print("Suffix strings with index are:")
    suffix_strings_array = []
    for i in range(len(s)):
        suffix_strings_array.append((s[i:], i))
    print(suffix_strings_array)
    sorted_array = sorted((s[i:], i) for i in range(len(s)))
    print("\nSorted suffix strings with index are:")
    print(sorted_array)
    print("\nFinal suffix array is:")
    suffix_array = [rank for suffix, rank in sorted((s[i:], i) for i in range(len(s)))]
    print(suffix_array)
    return suffix_array


generated_suffix_array = suffix_array_alternative_naive('banana')
