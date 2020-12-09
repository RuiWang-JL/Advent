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
l = 25
for i in range(len(lines)):
    d.append(int(lines[i]))
    if i < l:
        pass
    else:
        find(int(lines[i]),d)
        d.popleft()
