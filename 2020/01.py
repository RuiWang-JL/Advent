from itertools import combinations

with open('day1.txt', 'r+') as f:
    lines = [int(line.strip()) for line in f.readlines()]
    
for x, y in combinations(lines,2):
    if x+y == 2020: print('Part1:{}'.format(x*y)) 

for x, y, z in combinations(lines,3):
    if x+y+z == 2020: print('Part2:{}'.format(x*y*z)) 
