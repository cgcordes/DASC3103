#!/usr/bin/env python 3

import sys

lowest_totals = []

(last_key, total_sum) = (None, 0)
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    value = int(value) 
    if last_key and last_key != key:
        if len(lowest_totals) < 50 or total_sum < lowest_totals[-1][0]:
            lowest_totals.append((total_sum, last_key))
            lowest_totals.sort()

            lowest_totals = lowest_totals[:100]

        (last_key, total_sum) = (key, value)
    else:
        (last_key, total_sum) = (key, total_sum + value)

# Print the 100 lowest total sums and their corresponding keys
for total, key in lowest_totals:
    print("%s\t%s" % (key, total))