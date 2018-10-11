from quicksort import quicksort
from mergesort import mergesort
from randomized import randomized_quicksort
from median_3 import quicksort_3
from median_5 import quicksort_5

import time
import csv
import random
import sys
import copy

sys.setrecursionlimit(20000)
results = [1, 2, 3, 4, 5, 6, 1, 3, 4, 1, 10]
for i in range(10, 21):
    lst = [random.randint(1, 70) for j in range(2**i)]

    start = time.time()
    merge_count = mergesort(copy.deepcopy(lst))[1]
    end = time.time()
    merge_time = end - start
    #
    # start = time.time()
    # quick_count = quicksort(copy.deepcopy(lst), 0, (2 ** i) - 1, results[i%10])[1]
    # end = time.time()
    # quick_time = end - start

    start = time.time()
    rand_count = randomized_quicksort(copy.deepcopy(lst), 0, (2**i)-1)[1]
    end = time.time()
    rand_time = end - start

    start = time.time()
    med3_count = quicksort_3(copy.deepcopy(lst), 0, (2**i)-1)[1]
    end = time.time()
    med3_time = end - start

    start = time.time()
    med5_count = quicksort_5(copy.deepcopy(lst), 0, (2 ** i) - 1)[1]
    end = time.time()
    med5_time = end - start

    with open("file_count.csv", 'a') as file:
        results_writer = csv.writer(file, delimiter=',')
        results_writer.writerow(
            ['{}'.format(i)] + ['{}'.format(merge_count)] + ['{}'.format(rand_count)] + ['{}'.format(med3_count)] + ['{}'.format(med5_count)])
            # + ['{}'.format(quick_count)]

    with open("file_time.csv", 'a') as file:
        results_writer = csv.writer(file, delimiter=',')
        results_writer.writerow(['{}'.format(i)] + ['{}'.format(merge_time)] + ['{}'.format(rand_time)] + ['{}'.format(med3_time)] + ['{}'.format(med5_time)])
# + ['{}'.format(quick_time)]
