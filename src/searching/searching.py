# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    # Check to see if there is an end point
    if end is None:
        end = len(arr) - 1

    # Check to see if the starting point is greater then the end point
    if start > end:
        return -1

    # Create a midpoint
    mid = (start + end) // 2
    if target == arr[mid]:
        return mid

    # If the target value is LESS then the mid point, repeat the process only looking at the left hand side of the list
    if target < arr[mid]:
        return binary_search(arr, target, start, mid-1)

    return binary_search(arr, target, mid+1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
