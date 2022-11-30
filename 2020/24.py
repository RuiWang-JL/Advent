import re
from  itertools import product
from collections import defaultdict,deque,Counter
import time
import math
start_time = time.time()

with open('24.txt') as f:
    lines = [x.strip() for x in f.readlines()]

dirs = {'e':  2, 'se':  1 - 1j, 'sw': -1 - 1j, 'w': -2, 'nw': -1 + 1j, 'ne':  1 + 1j}
bla = set()
for line in lines:
    x = sum(dirs[ele] for ele in re.findall('(e|w|se|nw|sw|ne)',line))
    if x in bla:
        bla.remove(x)
    else:
        bla.add(x)
print(len(bla))

for i in range(100):
    nbla = set()
    tiles = {tile + dis for dis in dirs.values() for tile in bla}
    for tile in tiles:
        bla_nei = sum(tile+dis in bla for dis in dirs.values())
        if (tile in bla and 1<=bla_nei<=2) or (tile not in bla and bla_nei==2):
            nbla.add(tile)
    bla = nbla

print(len(bla))    

def part2():
    pass



print("--- %s seconds ---" % (time.time() - start_time))
