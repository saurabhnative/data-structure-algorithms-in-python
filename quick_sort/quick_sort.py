"""
Implement quick sort
Given an input array sort it in ascending order using quick sort
"""


# return right index of pivot element
def partition(input_array, low, high):
    pivot = input_array[high]
    i = low - 1
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if input_array[j] < pivot:
            i += 1
            # swap input_array[i] and input_array[j]
            input_array[i], input_array[j] = input_array[j], input_array[i]
    # swap input_array[i+1] and input_array[high]
    input_array[i+1], input_array[high] = input_array[high], input_array[i+1]
    return i + 1


# return sorted array using recursive calls
def quick_sort(input_array, low, high):
    if low < high:
        # pi is partitioning index
        pi = partition(input_array, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(input_array, low, pi - 1)
        quick_sort(input_array,pi + 1, high)


arr = [9, 7, 4, 3, 5]
n = len(arr)
print("Input array is: ",arr)
quick_sort(arr, 0, n-1)
print ("Sorted array is: ", arr)


"""
Worst case complexity: O(n²)
"""
