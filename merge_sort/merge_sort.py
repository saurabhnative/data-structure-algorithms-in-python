"""
Implement quick sort
Given an input array sort it in ascending order using quick sort
"""


# sort the array while merging it back to original size
def merge(input_array, left_half, right_half):
    i = j = k = 0
    # Copy data to temp arrays L[] and R[]
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            input_array[k] = left_half[i]
            i += 1
        else:
            input_array[k] = right_half[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left_half):
        input_array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        input_array[k] = right_half[j]
        j += 1
        k += 1


# recursively divide the array into half and then merge the array back
# sorting individual elements
def merge_sort(input_array):
    if len(input_array) > 1:
        middle = len(input_array) // 2
        left_half = input_array[:middle]
        right_half = input_array[middle:]
        merge_sort(left_half)
        merge_sort(right_half)
        merge(input_array, left_half, right_half)


arr = [2, 19, 21, 5, 6, 9]
print("Given array is: ", arr)
merge_sort(arr)
print("Sorted array is: ", arr)

"""
Complexity:- O(Nlog N)
"""
