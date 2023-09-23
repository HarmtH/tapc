#!/usr/bin/python3

import sys
import math

data = sys.stdin.readlines()
for line in data:
    print(10*math.tan(float(line)/180*math.pi))
