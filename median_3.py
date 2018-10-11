import sys

sys.setrecursionlimit(16000)


def quicksort_3(A, p, r):
    insertion_count, left_count, right_count, partition_count = 0, 0, 0, 0

    if p < r:
        parts = partition_3(A, p, r)
        q = parts[0]
        partition_count = parts[1]

        left_count = quicksort_3(A, p, q - 1)[1]
        right_count = quicksort_3(A, q + 1, r)[1]

    return A, left_count + right_count + insertion_count + partition_count


def partition_3(A, p, r):
    count, insertion_count = 0, 0
    shift = 0
    if len(A[p: r+1]) >= 3:
        pivots = [(p, A[p]), (r, A[r]), ((p + r) // 2, A[(p + r) // 2])]
        insertion_count = insertion_tuple(pivots)[1]
        for index, value in zip([p, (p + r) // 2, r], pivots):
            A[index] = value[1]
        A[(p + r) // 2], A[r - 1] = A[r - 1], A[(p + r )// 2]
        shift = 1

    pivot_index = r - shift
    pivot = A[r - shift]
    i = p - 1 + shift
    j = p + shift
    while j != pivot_index:
        count += 1
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1

    A[i + 1], A[pivot_index] = A[pivot_index], A[i + 1]
    i += 1
    return i, count + insertion_count


def insertion_tuple(lst):
    count = 0
    for i in range(1, len(lst)):
        value = lst[i][1]
        j = i
        count += 1

        while j > 0 and lst[j - 1][1] > value:
            count += 1
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1

    return lst, count


