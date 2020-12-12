import re
import numpy as np


with open('test6.txt') as f:
    data = f.read().strip()

groups = data.split('\n\n')
count = 0


for group in groups:
    count = count + len(set(group.replace('\n', '')))
print(count)

count = 0

for group in groups:
    count = count + len(set.intersection(*map(set, group.split('\n'))))
print(count)


        