from quicksort import quicksort
import time
import csv
import random
import sys
import copy

sys.setrecursionlimit(20000)

for i in range(17, 18):
    size_time = {}
    size_op = {}
    for j in range(1):
        lst = [random.randint(1, 70) for k in range(2**i)]

        for min_size in range(1, 20):

            start = time.time()
            sort_count = quicksort(copy.deepcopy(lst), 0, 2**i-1, min_size)[1]
            end = time.time()
            sort_time = end - start
            print(min_size, sort_time)
            # if min_size in size_time:
            #     size_time[min_size] = size_time[min_size].append(sort_time)
            # else:
            #     size_time[min_size] = [sort_time]


            # size_time[min_size] = size_time.setdefault(min_size, []).append(sort_time)
            # size_op[min_size] = size_op.setdefault(min_size, []).append(sort_count)



    with open("results.csv", 'a') as file:
        results_writer = csv.writer(file, delimiter=',')
        results_writer.writerow(size_time)
        results_writer.writerow(size_op)





