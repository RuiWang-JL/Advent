import numpy as np
with open('day.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]

k = np.empty((10, 10), int)
for x, line in enumerate(lines):
    for y, ele in enumerate(line):
        k[x][y] = int(ele)

k = np.pad(k, pad_width=1, constant_values=0)
neigh = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
         (0, 1), (1, -1), (1, 0), (1, 1)]


def flashoneround(toflash):
    flashed.update(toflash)
    newtoflash = set()
    for ele in toflash:
        flash(ele[0], ele[1], newtoflash)
    return newtoflash


def flash(x, y, newtoflash):
    k[x][y] = 0
    for dx, dy in neigh:
        if (x+dx, y+dy) not in flashed and 0 < x+dx < 11 and 0 < y+dy < 11:
            k[dx+x][dy+y] += 1
        if k[dx+x][dy+y] > 9 and (x+dx, y+dy) not in flashed:
            newtoflash.add((dx+x, dy+y))


tot = 0
step = 0
for i in range(1000):
    toflash = set()
    flashed = set()
    # step1: add 1
    for x in range(1, 11):
        for y in range(1, 11):
            k[x][y] += 1
            # check which one will flash directly
            if k[x][y] > 9 and (x, y) not in flashed:
                toflash.add((x, y))
    # flash more round until everything has flashed
    while len(toflash) > 0:
        toflash = flashoneround(toflash)
    tot += len(flashed)
    if len(flashed) == 100:
        print(i+1)
        break
print(tot)
