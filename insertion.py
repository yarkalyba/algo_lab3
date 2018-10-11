def insertionsort(lst, p, r):
    count = 0
    sort_list = lst[p:r+1]

    for i in range(1, len(sort_list)):
        value = sort_list[i]
        j = i
        count += 1

        while j > 0 and sort_list[j-1] > value:
            count += 1
            sort_list[j] = sort_list[j - 1]
            j -= 1
        sort_list[j] = value

    lst[p:r+1] = sort_list
    return lst, count