
from collections import defaultdict
with open('day5.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]

vents = defaultdict(int)

for line in lines:
    a, b = line.split("->")
    a = a.strip().split(",")
    a1 = int(a[0])
    a2 = int(a[-1])
    b = b.strip().split(",")
    b1 = int(b[0])
    b2 = int(b[-1])
    dx = abs(a1-b1)
    dy = abs(a2-b2)
    if dx == 0:
        for x in range(dy+1):
            ele = x + min(a2, b2)
            vents[(ele, a1)] += 1
    elif dy == 0:
        for y in range(dx+1):
            ele = y + min(a1, b1)
            vents[(a2, ele)] += 1
    elif abs(dx) == abs(dy):
        if a1 < b1:
            xl = range(a1, b1+1)
        else:
            xl = range(a1, b1-1, -1)
        if a2 < b2:
            yl = range(a2, b2+1)
        else:
            yl = range(a2, b2-1, -1)
        for i in range(len(xl)):
            vents[(yl[i], xl[i])] += 1
tot = 0
for key, va in vents.items():
    if va > 1:
        tot += 1
print(tot)
