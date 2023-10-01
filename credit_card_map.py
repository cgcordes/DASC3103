#!/usr/bin/env python 3

import sys
for index, row in sys.stdin.iterrows():
    ID = row[0]
    y = row[24]
    for i in range(6, 12):
        value_at_xi = row[i]
        output = "%s\t%s" % (ID, value_at_xi)
        print(output)