import re
import numpy as np
from collections import deque
from itertools import combinations

with open('day9.txt') as f:
    lines = [int(x.strip()) for x in f.readlines()]

d = deque()
l = 25
#1
for i,line in enumerate(lines):
    d.append(line)
    if i < l:
        pass
    else:
        if not any(sum(a) == line for a in combinations(d,2)):
            part1 = line
            print(part1)
            break
        d.popleft()
#2
for n in range(2,len(lines)):
    for i in range(len(lines)-n):
        s = lines[i:i+n]
        if sum(s) == part1:
            print(min(s) + max(s))
            quit()