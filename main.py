from quicksort import quicksort
import time
import csv
import random
import sys
import copy

sys.setrecursionlimit(20000)
num_experiments = 5
for i in range(10, 21):
    size_time = {}
    size_op = {}
    for j in range(num_experiments):
        lst = [random.randint(1, 70) for k in range(2**i)]

        for min_size in range(1, 30):

            start = time.time()
            sort_count = quicksort(copy.deepcopy(lst), 0, 2**i-1, min_size)[1]
            end = time.time()
            sort_time = end - start

            if min_size in size_time:
                size_time[min_size].append(sort_time)
            else:
                size_time[min_size] = [sort_time]

            if min_size in size_op:
                size_op[min_size].append(sort_count)
            else:
                size_op[min_size] = [sort_count]

    with open("results_time.csv", 'a') as file:
        results_writer = csv.writer(file)
        results_writer.writerow(['size {}'.format(i)])
        for key, value in size_time.items():
            results_writer.writerow(['{}'.format(key)] + ['{}'.format(sum(value)/num_experiments)])

    with open("results_op.csv", 'a') as file:
        results_writer = csv.writer(file, delimiter=',')
        results_writer.writerow(['size {}'.format(i)])
        for key, value in size_op.items():
            results_writer.writerow(['{}'.format(key)] + ['{}'.format(sum(value)/num_experiments)])