#!/usr/bin/python3

import sys
import math

data = sys.stdin.readlines()
h, w = map(int, data[0].split(' '))

grid = list(map(str.rstrip, data[1:]))

found = False
for i in range(4):
    grid = list(zip(*grid[::-1]))
    # for line in grid:
    #     for c in line:
    #         print(c, end='')
            # if c == '.': print('#', end='')
            # elif c == '#': print('.', end='')
            # else: print('wtf')
        # print('')
    # print(grid)
    lmin = ''.join(grid[0]).find('#')
    rmax = ''.join(grid[0]).rfind('#')
    impossible = False
    holes = set()
    if any([c == '.' for c in grid[0][lmin:rmax]]):
        impossible = True
    for line in grid:
        # print('lmin=', lmin)
        # print('rmax=', rmax)
        l = ''.join(line).find('#')
        r = ''.join(line).rfind('#')
        if l < lmin:
            impossible = True
        if r > rmax:
            impossible = True
        newholes = {i for i in range(l, r-l) if line[i] == '.'}
        if holes.issubset(newholes):
            holes = newholes
        else:
            impossible = True
        lmin = l
        rmax = r
    # print('lmin=', lmin)
    # print('rmax=', rmax)
    # print(impossible)
    if not impossible:
        # print('found one')
        # print(grid)
        print(str(len(grid)) + ' ' + str(len(grid[0])))
        for line in grid:
            for c in line:
                # print(c, end='')
                if c == '.': print('#', end='')
                elif c == '#': print('.', end='')
                else: print('wtf')
            print('')
        found = True
        break
if not found:
    print('impossible')
