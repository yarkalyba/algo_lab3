import math

def mergesort(lst):
    print(type(lst))
    n = len(lst)
    if n == 1:
        return lst

    left = mergesort(lst[:n // 2])
    right = mergesort(lst[n // 2:])
    lst = merge(left, right)
    return lst


def merge(left, right):
    len_left = len(left)
    len_right = len(right)
    lst = []

    left.append(math.inf)
    right.append(math.inf)

    i, j = 0, 0
    for k in range(len_right + len_left):

        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1

    return lst
