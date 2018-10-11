import sys
sys.setrecursionlimit(16000)

def quicksort_5(A, p, r):
    insertion_count, left_count, right_count, partition_count = 0, 0, 0, 0

    if p<r:
        parts = partition_5(A, p, r)
        q = parts[0]
        partition_count = parts[1]

        left_count = quicksort_5(A, p, q-1)[1]
        right_count = quicksort_5(A, q+1, r)[1]

    return A, left_count + right_count + insertion_count + partition_count


def partition_5(A, p, r):
    count, insertion_count = 0, 0
    shift = 0
    print("a before partition", A)
    if len(A[p: r]) >= 5:
        pivots = [(p, A[p]),
                  ((3*p+r)//4, A[(3*p+r)//4]),
                  ((p+r)//2, A[(p+r)//2]),
                  ((p + 3*r)//4, A[(p + 3*r)//4]),
                  (r, A[r])]

        insertion_count = insertion_tuple(pivots)
        for index, value in zip([p, (3*p+r)//4, p+r//2, (p + 3*r)//4, r], pivots):
            A[index] = value[1]

        print(len(A), p, r)
        A[p+1], A[(3*p+r)//4] = A[(3*p+r)//4], A[p+1]
        A[r-1], A[(3*r+p)//4] = A[(3*r+p)//4], A[r-1]
        print(A[r-2], A)
        A[p+r//2], A[r-2] = A[r-2], A[p+r//2]
        print(A[r-2], A)
        shift = 2
    print('A after 5', A)
    pivot_index = r - shift
    pivot = A[pivot_index]
    i = p - 1 + shift
    j = p + shift

    while j != pivot_index:
        count += 1
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1

    A[i+1], A[pivot_index] = A[pivot_index], A[i+1]
    i += 1
    print('A after partition', A)
    return i, count+insertion_count


def insertion_tuple(lst):
    count = 0
    for i in range(1, len(lst)):
        value = lst[i][1]
        j = i
        count += 1

        while j > 0 and lst[j - 1][1] > value:
            count += 1
            lst[j], lst[j-1] = lst[j - 1], lst[j]
            j -= 1

    return count

print(quicksort_5([3, 10, 2, 4, 1, 0, 9, -1, 5, 2, 2], 0, 10))