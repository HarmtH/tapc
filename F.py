#!/usr/bin/python3

import sys
import math

data = sys.stdin.readlines()
num_types = int(data[0])
forks = map(int, data[1].split(' '))
sorted_forks = sorted(forks)
print(sorted_forks[0]+sorted_forks[1])
