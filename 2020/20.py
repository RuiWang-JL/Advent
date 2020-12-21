from  itertools import product, combinations
import time
from collections import defaultdict
import numpy as np

start_time = time.time()

with open('test.txt') as f:
    lines = [x.strip() for x in f.readlines()]

tiles = defaultdict(list)

for i, line in enumerate(lines):
    if i%12 == 0:
        tid = line[5:9]
    elif 1 <= i%12 <= 10:
        tiles[tid].append(list(line))
    else:
        
def part2():
    print(lines)
part2()
#     lines = [x.strip() for x in f.readlines()]

# tiles = defaultdict(set)
# flipt = defaultdict(set)
# top,left,right,bottom = '','','',''

# for i, line in enumerate(lines):  
#     if i%12 == 0:
#         tid = line[5:9]
#     elif i%12 == 1:
#         top = line
#         left = line[0]
#         right = line[9]
#     elif 2 <= i%12 <= 9:
#         left += line[0]
#         right += line[9]
#     elif i%12 == 10:
#         bottom = line
#         left += line[0]
#         right += line[9]
#         tiles[tid] = {top,right,bottom,left}
#     else:
#         top,left,right,bottom = '','','',''
    
# for key in tiles.keys():
#     for dire in tiles[key]:
#         flipt[key].add(dire[::-1])

# def part1():
#     tot = 1
#     for key in tiles.keys():
#         cnt = 0
#         for co_key in tiles.keys():
#             if key != co_key:
#                 if not tiles[key].isdisjoint(tiles[co_key]) or not tiles[key].isdisjoint(flipt[co_key]):   
#                     cnt +=1
#         if cnt ==2:
#             print(cnt,key)  
#             tot *= int(key)  
#     print(tot)



print("--- %s seconds ---" % (time.time() - start_time))
