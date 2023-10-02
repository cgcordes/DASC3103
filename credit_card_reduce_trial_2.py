#!/usr/bin/env python 3

import sys

data = []
(last_key, total_sum) = (None, 0)
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    value = int(value)
    if last_key and last_key != key:
        data.append((last_key, total_sum))
        (last_key, total_sum) = (key, value)
    else:
        (last_key, total_sum) = (key, total_sum + value)
if last_key:
    data.append((last_key, total_sum))

data.sort(key=lambda x: x[1], reverse=True)

# Print the top 50 highest total_sum values.
for i, (key, total_sum) in enumerate(data[:50], 1):
    print(f"{i}. {key}\t{total_sum}")