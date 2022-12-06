import numpy as np
import copy
from collections import deque
# with open('test.txt', 'r+') as f:
with open('06.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        for idx in range(14, len(line)):
            if len(set(line[idx-14:idx])) == 14:
                print(idx)
                break
