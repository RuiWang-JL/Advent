import time
from itertools import combinations
from collections import Counter
start_time = time.time()

with open('day2.txt') as f:
    lines = [x.strip() for x in f.readlines()]

# count()
def part1():
    tot2,tot3 = 0,0
    for line in lines:
        two, three = False, False
        for ele in set(line):
            if line.count(ele) == 2: two = True
            elif line.count(ele) == 3 : three = True
        if two: tot2+=1
        if three: tot3+=1
    print(tot2*tot3)    

# Collections Counter
def part1_1():
    tot2,tot3 = 0,0
    for line in lines:
        if 2 in Counter(line).values(): tot2+=1
        if 3 in Counter(line).values(): tot3+=1
    print(tot2*tot3)  

def part2():
    for a,b in combinations(lines,2):
        count = 0
        for x,y in zip(a,b):
            if x!=y:count+=1
        if count ==1:
            new = ''
            for x,y in zip(a,b):
                if x==y:new+=x
            print(new)
            break
# Shorter?
def part2_1():
    for a,b in combinations(lines,2):
       if sum([x!=y for x, y in zip(a,b)]) == 1:
           print(''.join([(x) for x,y in zip(a,b) if x==y]))
           break

part2_1()
print("--- %s seconds ---" % (time.time() - start_time))