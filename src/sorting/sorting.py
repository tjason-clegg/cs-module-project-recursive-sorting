# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Index all elements and loop
    a = 0
    b = 0
    while (a + b < elements):
        # Merge when index a and index b is equal to length
        if a >= len(arrA):
            merged_arr[a + b] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[a + b] = arrA[a]
            a += 1
        # Sort -> Swap if smaller than other arr index
        elif arrA[a] < arrB[b]:
            merged_arr[a + b] = arrA[a]
            a += 1
        elif arrA[a] >= arrB[b]:
            merged_arr[a + b] = arrB[b]
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # If it is only one element in the list it is already sorted, return.
    if len(arr) <= 1:
        return arr

        # Fivide the list recursively into two halves until it can no more be divided.
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    # Merge the smaller lists into new list in sorted order.
    arr = merge(left, right)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
