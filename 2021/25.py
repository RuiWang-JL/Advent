import numpy as np
import copy
with open('day25.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
ymx = len(lines)
xmx = len(lines[0])
sea = np.empty((len(lines), len(lines[0])), str)
for y, line in enumerate(lines):
    for x, ele in enumerate(line):
        sea[y][x] = ele


def move(sea):
    count = 0
    newsea = copy.deepcopy(sea)
    # east first
    for y in range(ymx):
        for x in range(xmx):
            if sea[y][x] == ">":
                # check right
                rightx = (x+1) % xmx
                if sea[y][rightx] == ".":
                    count += 1
                    newsea[y][x] = "."
                    newsea[y][rightx] = ">"
    sea = copy.deepcopy(newsea)
    # south then
    for y in range(ymx):
        for x in range(xmx):
            if sea[y][x] == "v":
                # check down
                downy = (y+1) % ymx
                if sea[downy][x] == ".":
                    count += 1
                    newsea[y][x] = "."
                    newsea[downy][x] = "v"
    return newsea, count


i = 0
while True:
    i += 1
    newsea, cnt = move(sea)
    sea = copy.deepcopy(newsea)
    # print("After i step:", i, cnt)
    if cnt == 0:
        print("part1:", i)
        break
