import numpy as np
import re
from collections import defaultdict


colors = defaultdict(list)
colors_count = defaultdict(list)

with open('day7.txt') as f:
    lines = [x.strip() for x in f.readlines()]

for line in lines:
    parent = ' '.join(line.split()[:2])
    for count, child in re.findall(r"(\d+) ([a-z ]+) bags?", line):
        colors[child].append(parent)
        colors_count[parent].append((child, int(count)))
# 1
parents = set()
def find_parent(child):
    parents.add(child)
    for parent in colors[child]:
        find_parent(parent)
find_parent('shiny gold')
print(len(parents)-1)
# 2
def count_bags(parent):
    return sum((count * (1+count_bags(child))) for child, count in colors_count[parent])

print(count_bags('shiny gold'))
