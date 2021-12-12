from collections import Counter, defaultdict


with open('day12.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
a = defaultdict(set)
starts = set()
ends = set()

for line in lines:
    eles = line.split("-")
    for ele in eles:
        a[eles[0]].add(eles[1])
        a[eles[1]].add(eles[0])


def bfs():
    tot = 0
    queue = []
    queue.append(["start"])
    while queue:
        curpath = queue.pop(0)
        cur = curpath[-1]
        used = False
        counts = Counter(curpath)
        for key, v in counts.items():
            if v > 1 and key.islower():
                used = True
        if cur == "end":
            tot += 1
            continue
        for nei in a[cur]:
            if nei.islower() and curpath.count(nei) == 2:
                continue
            elif nei.islower() and curpath.count(nei) == 1 and used:
                continue
            elif nei == "start":
                continue
            elif nei == "end" and curpath.count(nei) == 1:
                continue
            queue.append(curpath+[nei])
    print(tot)


bfs()
