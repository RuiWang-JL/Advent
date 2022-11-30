from  itertools import product, combinations
import time
from collections import defaultdict
import numpy as np

start_time = time.time()

# From part1() test
# 1951
# 1171
# 2971
# 3079
# From part1() input
# 3467
# 3169
# 1019
# 1249
with open('test.txt') as f:
    lines = [x.strip() for x in f.readlines()]

tiles = defaultdict(list)

for i, line in enumerate(lines):
    if i%12 == 0:
        tid = line[5:9]
    elif 1 <= i%12 <= 10:
        tiles[tid].append(list(line))

#print(a[0,]) 1st row
#print(a[-1,]) last row

cur = '1951'

for ele in tiles:
    ca = np.array(tiles[cur])
    ma = np.array(tiles[ele])
    for i,edge in enumerate([ca[0,],ca[:,-1],ca[-1,],ca[:,0],np.flip(ca[0,]),np.flip(ca[:,-1]),np.flip(ca[-1,]),np.flip(ca[:,0])]):
        for j,match in enumerate([ma[0,],ma[:,-1],ma[-1,],ma[:,0],np.flip(ma[0,]),np.flip(ma[:,-1]),np.flip(ma[-1,]),np.flip(ma[:,0])]):
            if str(edge) == str(match):
                print(str(edge),str(match))
# for ele1,ele2 in combinations(tiles,2):
#     top,right,down,left = tiles[ele1][0,],tiles[ele1]

def part2():
    arr = np.array(tiles['3079'])
    #narr = np.flipud(arr)
    #rarr = np.rot90(arr)
    #print(len(tiles))
    #print(rarr)
    #print(narr)
    #print(arr)
    #print(tiles['3079'])
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
#             print(key)  
#             tot *= int(key)  
#     print(tot)

# part1()

print("--- %s seconds ---" % (time.time() - start_time))
