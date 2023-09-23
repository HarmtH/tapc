#!/usr/bin/python3

import sys
import math

data = sys.stdin.readlines()
sides_on_dice = int(data[0])
nums_dice_1 = list(map(int, data[1].split(' ')))
nums_dice_2 = list(map(int, data[2].split(' ')))

d1_wins=0
d2_wins=0
for d1 in nums_dice_1:
    for d2 in nums_dice_2:
        if d1 > d2:
            d1_wins += 1
        elif d2 > d1:
            d2_wins += 1

if d1_wins > d2_wins:
    print('first')
elif d1_wins == d2_wins:
    print('tie')
else:
    print('second')
