import re
import numpy as np
from collections import deque

def find(x, nums):
    nums_need = []
    for ele in nums:
        if ele < x/2:
            nums_need.append(x-ele)
    if not (set(nums_need) & set(nums)):
        print(x)

with open('day9.txt') as f:
    lines = [x.strip() for x in f.readlines()]
d = deque()

for line in lines:
    d.append(int(line))

for n in range(2,len(lines)):
    for i in range(len(lines)-n):
        newset = set()
        newset.clear()
        total = sum(d[i+n] for n in range(0,n))
        for x in range(0,n):
            newset.add(d[x+i])
        if total == 530627549:
            print(newset)
            print(min(newset)+max(newset))
