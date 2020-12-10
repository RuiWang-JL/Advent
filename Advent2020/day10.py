import re
import numpy as np
from collections import deque, defaultdict
from itertools import product

with open('day10.txt') as f:
    lines = [int(x.strip()) for x in f.readlines()]

lines = sorted(lines)
max_num = max(lines) + 3
lines = lines + [max_num]

path = defaultdict(int)
#recuision
def from_v_to_max(v):
    if v in path:return path[v]
    if v == max_num: return 1
    else:
        num = 0
        for x in range(v+1, v+4):
            if x in lines: num += from_v_to_max(x)
        path[v] = num
        return path[v]
#print(from_v_to_max(0))
#print(path)
path.clear()
#reverse
lines.reverse()
for line in lines:
    num = 0
    if line == max_num:
        num=1
    if (line+1) in lines:
        num += path[line+1]
    if (line+2) in lines:
        num += path[line+2]
    if (line+3) in lines:
        num += path[line+3]
    path[line] = num
#print(path[0])

#loop
path.clear()
lines.reverse()
for line in lines:
    num = 0
    if line == 0:
        num=0
    if line == 1:
        num= 1
    if line ==2:
        num = path[1]+1
    if line ==3:
        num = path[2]+path[1]+1
    if line >3:
        if (line-1) in lines:
            num += path[line-1]
        if (line-2) in lines:
            num += path[line-2]
        if (line-3) in lines:
            num += path[line-3]
    path[line] = num
print(path[max_num])

