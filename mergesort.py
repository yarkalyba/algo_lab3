import math

def mergesort(lst):

    n = len(lst)
    if n == 1:
        return lst, 0

    left, count_left = mergesort(lst[:n // 2])
    right, count_right = mergesort(lst[n // 2:])
    lst, count_merge = merge(left, right)
    return lst, count_left + count_right + count_merge


def merge(left, right):
    count = 0
    len_left = len(left)
    len_right = len(right)
    lst = []

    left.append(math.inf)
    right.append(math.inf)

    i, j = 0, 0
    for k in range(len_right + len_left):
        count += 1
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1

    return lst, count
