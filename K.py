#!/usr/bin/python3

import sys
import math

data = sys.stdin.readlines()
num_castles = int(data[0])
castles = []
for line in data[1:]:
    castles.append(list(map(int, line.split(' '))))

# print(castles)

min_distance = 99999999999999999
for castle in castles:
    sum_this_one = 0
    for destination in castles:
        if castle == destination:
            pass
        sum_this_one += math.sqrt(((castle[0]-destination[0])**2)
                                 +((castle[1]-destination[1])**2))
    if sum_this_one < min_distance:
        min_distance = sum_this_one
print(min_distance/(num_castles-1))
