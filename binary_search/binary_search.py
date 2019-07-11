"""
Implement binary search
Given an input array and target element search
for that element using binary search
"""

# return index of target element or None
def binary_search(input_array, target):
    # define lower and higher indices for starting search
    lower_index = 1
    higher_index = len(input_array)
    while lower_index != higher_index:
        mid = int(abs(lower_index + (higher_index - lower_index)/2))
        if input_array[mid] == target:
            return mid
        elif input_array[mid] < target:
            lower_index = mid + 1
        else:
            higher_index = mid


input_array = [1, 3, 5, 7, 9]
target = 9
print("Element found at position", binary_search(input_array, target), "in array")

# Output: Element found at position 4 in array

"""
Complexity:- O(log N)
"""







