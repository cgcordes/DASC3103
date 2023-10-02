#!/usr/bin/env python 3

import sys

lowest_totals = []

# Process input from standard input
(last_key, total_sum) = (None, 0)
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    value = int(value) 
    if last_key and last_key != key:
        # Check if the current total_sum is lower than the lowest of the 50 lowest totals
        if len(lowest_totals) < 50 or total_sum < lowest_totals[-1][0]:
            # Append the current total_sum and key to the list and keep it sorted
            lowest_totals.append((total_sum, last_key))
            lowest_totals.sort()

            # Keep only the 50 lowest totals
            lowest_totals = lowest_totals[:50]

        (last_key, total_sum) = (key, value)
    else:
        (last_key, total_sum) = (key, total_sum + value)

# Print the 50 lowest total sums and their corresponding keys
for total, key in lowest_totals:
    print("%s\t%s" % (key, total))