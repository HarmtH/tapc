#!/usr/bin/python3

import sys
import math

data = sys.stdin.readlines()
cur = data[1]
new = data[2]

res = 0
for i in range(int(data[0])):
    g1=ord(cur[i])-64
    g2=ord(new[i])-64
    diff=[abs(g1-g2),
          abs((g1+26)-g2),
          abs(g1-(g2+26))]
    res += min(diff)
print(res)
