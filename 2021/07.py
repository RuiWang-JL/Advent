from collections import Counter
from collections import Counter
import collections
with open('day7.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
line = [int(ele) for ele in lines[0].split(',')]
minPos = min(line)
maxPos = max(line)
res = []
for i in range(minPos, maxPos+1):
    dis = [abs(i-ele) for ele in line]
    c = collections.Counter(dis)
    tot1 = 0
    for a, coun in c.items():
        x = 0
        for k in range(a+1):
            x += k
        tot = coun*(x)
        tot1 += tot
    res.append(tot1)
print(min(res))
