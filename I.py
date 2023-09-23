#!/usr/bin/python3

import sys
import math

data = sys.stdin.readlines()
num_jobs, num_cores = map(int, data[0].split(' '))
durations = list(reversed(list(map(int, data[1].split(' ')))))

last_message_time = 0
max_time_without = 0
running_jobs = [99999]*num_cores

for i in range(num_cores):
    if len(durations):
        running_jobs[i] = durations.pop()
    else:
        running_jobs[i] = None

t = 1
while True:
    for i in range(len(running_jobs)):
        if running_jobs[i] is not None:
            running_jobs[i] -= 1
        if running_jobs[i] == 0:
            new_time_without = t - last_message_time
            if new_time_without > max_time_without:
                max_time_without = new_time_without
            last_message_time = t
            if len(durations):
                running_jobs[i] = durations.pop()
            else:
                running_jobs[i] = None
    if all(map(lambda x: x is None, running_jobs)):
        break
    t += 1
print(max_time_without)
