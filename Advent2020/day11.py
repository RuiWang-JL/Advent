import re
import numpy as np
from collections import deque, defaultdict
from itertools import product
import copy

with open('day11.txt') as f:
    lines = [list(x.strip()) for x in f.readlines()]

x0=['.']*(len(lines[0])+2)

l=[]
l.append(x0)  
for line in lines:
    line = ['.'] + line + ['.']
    l.append(line)
l.append(x0) 


def check(l0):
    l1=copy.deepcopy(l0)
    changed = False
    for y,x in product(range(1,len(l0)-1),range(1, len(l0[0])-1)):
        sea = 0
        for j,i in product(range(-1,2),range(-1,2)):
                if j==0 and i==0:
                    continue         
                if l0[y+j][x+i] == '#':
                    sea = sea +1    
        
        if l0[y][x] == 'L' and sea == 0:
            l1[y][x] = '#'
            changed = True
        elif l0[y][x] == '#' and sea >= 4:
            l1[y][x] = 'L'
            changed = True

    if changed:
        check(l1)
    else:      
        print(sum(row.count('#') for row in l1))
        return l1

check(l)
