from insertion import insertionsort

def quicksort(A, p, r, min_size):
    insertion_count, left_count, right_count, partition_count = 0, 0, 0, 0

    if r-p+1<=min_size and p<r:
        insertion_count = insertionsort(A, p, r)[1]
    elif p<r:
        parts = partition(A, p, r)
        q = parts[0]
        partition_count = parts[1]
        left_count = quicksort(A, p, q-1, min_size)[1]
        right_count = quicksort(A, q+1, r, min_size)[1]
    return A, left_count + right_count + insertion_count + partition_count


def partition(A, p, r):
    count = 0
    pivot = A[r]
    i = p-1
    j = p
    while j != r:
        count += 1
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1
    A[i+1], A[r] = A[r], A[i+1]
    i += 1
    return i, count

# print(quicksort([3, 2, 1], 0, 2, 0))
# print(quicksort([1, 4, 3, 5, 2, 7, -1, 9, 100, -400, 7], 0, 10, 3))