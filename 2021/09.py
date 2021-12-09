import numpy as np
with open('day9.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
yy = len(lines)
xx = len(lines[0])
k = np.empty((yy, xx), int)
for i, x in enumerate(lines):
    for j, y in enumerate(x):
        k[i][j] = int(y)
kk = np.pad(k, pad_width=1, constant_values=9)
tot = 0
lowest = set()
for i in range(1, yy+1):
    for j in range(1, xx+1):
        if kk[i][j] < kk[i-1][j] and kk[i][j] < kk[i+1][j] and kk[i][j] < kk[i][j-1] and kk[i][j] < kk[i][j+1]:
            tot += kk[i][j]+1
            lowest.add((i, j))

# part2


def neighbors(x, y):
    return {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}


def dfs(x, y, val, visited):
    if (x, y) in visited or val == 9:
        return
    else:
        visited.add((x, y))
    for xx, yy in neighbors(x, y):
        dfs(xx, yy, kk[xx][yy], visited)


alll = []
for x, y in lowest:
    visited = set()
    dfs(x, y, kk[x][y], visited)
    alll.append(len(visited))

alll.sort()
print(alll[-1]*alll[-2]*alll[-3])
