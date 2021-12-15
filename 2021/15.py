import numpy as np
with open('day15.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]

w = 100
k = np.empty((w, w), int)
for x, line in enumerate(lines):
    for y, ele in enumerate(line):
        k[x][y] = int(ele)
n = ((0, 1), (0, -1), (1, 0), (-1, 0))
# n = ((0, 1), (1, 0))
nw = w*5
nk = np.empty((5*w, 5*w), int)
for x in range(nw):
    for y in range(nw):
        px, xx = divmod(x, w)
        py, yy = divmod(y, w)
        nk[x][y] = (k[xx][yy] + px+py - 1) % 9 + 1
# print(nk)


def find_shortest_path(k, w):
    que = []
    que.append((0, 0, 0))
    visited = set()
    visited.add((0, 0))
    while(que):
        que.sort()
        dis, x, y = que.pop(0)
        if x == w-1 and y == w-1:
            return dis
        for dx, dy in n:
            xx, yy = x+dx, y + dy
            if xx < 0 or xx >= w or yy < 0 or yy >= w:
                continue
            if(xx, yy) not in visited:
                visited.add((xx, yy))
                que.append((dis + k[xx][yy], xx, yy))


print(find_shortest_path(k, w))
print(find_shortest_path(nk, nw))
