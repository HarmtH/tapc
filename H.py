#!/usr/bin/python3

import sys
import math

data = sys.stdin.readlines()
num_lines = int(data[0])

order = []
for line in data[1:]:
    if line[0] in order:
        if line[0] != order[-1]:
            print('impossible')
            sys.exit(0)
    else:
        order.append(line[0])

print(''.join(order))
