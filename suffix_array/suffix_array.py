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

print("Input string is: banana\n")
generated_suffix_array = suffix_array_alternative_naive('banana')


"""
Output:
Input string is: banana

Suffix strings with index are:
[('banana', 0), ('anana', 1), ('nana', 2), ('ana', 3), ('na', 4), ('a', 5)]

Sorted suffix strings with index are:
[('a', 5), ('ana', 3), ('anana', 1), ('banana', 0), ('na', 4), ('nana', 2)]

Final suffix array is:
[5, 3, 1, 0, 4, 2]
"""