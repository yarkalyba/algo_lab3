import random

def randomized_quicksort(A, p, r):
    left_count, right_count, partition_count = 0, 0, 0
    if p<r:
        parts = randomized_partition(A, p, r)
        q = parts[0]
        partition_count = parts[1]
        left_count = randomized_quicksort(A, p, q-1)[1]
        right_count = randomized_quicksort(A, q+1, r)[1]
    return A, left_count + right_count + partition_count


def randomized_partition(A, p, r):
    count = 0
    pivot_index = random.randint(p, r)
    A[r], A[pivot_index] = A[pivot_index], A[r]
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
