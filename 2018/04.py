from  itertools import product
import time
import re
from collections import defaultdict

start_time = time.time()

with open('18.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    lines.sort(key=lambda e : e[1:17])

def part1():
    a = defaultdict(list)
    a_sum = defaultdict(list)
    guard = 0
    max_guard = 0
    for line in lines:
        if "Guard" in line:
            guard = int(re.search("#[0-9]+",line).group(0)[1:])
        elif 'falls asleep' in line:
            start = int(re.search(':[0-9]+',line).group(0)[1:])
        elif 'wakes up' in line:
            end = int(re.search(':[0-9]+',line).group(0)[1:])
            a[guard].append((start,end))
    for elem in a.keys():
        a_sum[elem] = sum([(end-start) for start, end in a[elem]])
    max_guard = max(a_sum, key=a_sum.get)
    cnt = defaultdict(int)
    for start, end in a[max_guard]:
        for i in range(start, end):
            cnt[i] += 1
    max_minute = max(cnt,key=cnt.get)
    print(max_guard*max_minute)

def part2():
    a = defaultdict(lambda: defaultdict(int))
    b = {}
    guard = 0
    max_guard = 0
    for line in lines:
        if "Guard" in line:
            guard = int(re.search("#[0-9]+",line).group(0)[1:])
        elif 'falls asleep' in line:
            start = int(re.search(':[0-9]+',line).group(0)[1:])
        elif 'wakes up' in line:
            end = int(re.search(':[0-9]+',line).group(0)[1:])
            for i in range(start, end):
                (a[guard])[i] += 1
    for guard in a.keys():
        b[guard]=(max(a[guard].values()),max(a[guard],key=a[guard].get))
    max_guard = max(b, key=b.get)
    print(max_guard*b[max_guard][1])
            

part2()

print("--- %s seconds ---" % (time.time() - start_time))

