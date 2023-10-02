#!/usr/bin/env python 3

import sys

(last_key, total_sum) = (None, 0)
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    value = int(value) 
    if last_key and last_key != key:
        print("%s\t%s" % (last_key, total_sum))
        (last_key, total_sum) = (key, value)
    else:
        (last_key, total_sum) = (key, total_sum + value)    
if last_key:
    print("%s\t%s" % (last_key, total_sum))