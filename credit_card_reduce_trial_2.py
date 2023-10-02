#!/usr/bin/env python 3

import sys

(last_key, total_sum, count) = (None, 0, 0)
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    value = int(value) 
    if last_key and last_key != key:
        print("%s\t%s\t%s" % (last_key, total_sum, count))
        (last_key, total_sum, count) = (key, value, 1)
    else:
        (last_key, total_sum, count) = (key, total_sum + value, count + 1)    
if last_key:
    print("%s\t%s\t%s" % (last_key, total_sum, count))