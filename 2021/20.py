
import numpy as np
with open('day20.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
algorithm = lines[0]
first = algorithm[0]
last = algorithm[-1]
###
###
###
# "111111111" => "."

print(first, last)
input = lines[2:]
w = len(input)
k = len(input[0])
IN = np.empty((w, w), str)
for y, line in enumerate(input):
    for x, ele in enumerate(line):
        if ele == ".":
            IN[y][x] = "0"
        else:
            IN[y][x] = "1"


def flash(IN, padstringvalue):
    w = len(IN)
    out = np.empty((w+2, w+2), str)
    # newin = 5+2+2 =9: 1,2,....,7
    # .. (#..#.) ..
    IN1 = np.pad(IN, pad_width=1, constant_values=padstringvalue)
    # .. (#..#.) ..
    newin = np.pad(IN1, pad_width=1, constant_values=padstringvalue)
    for y in range(1, 3+w):  # 1,7
        for x in range(1, 3+w):
            bstr = ""
            for yy in [y-1, y, y+1]:  # 0,1,2    6,7,8
                for xx in [x-1, x, x+1]:
                    bstr += newin[yy][xx]
            bint = int(bstr, 2)
            if algorithm[bint] == ".":
                out[y-1][x-1] = "0"
            elif algorithm[bint] == "#":
                out[y-1][x-1] = "1"
    return out


def count(out):
    tot = 0
    for line in out:
        for ele in line:
            if ele == "1":
                tot += 1
    return tot


for i in range(50):
    if i % 2 == 0:
        pad = "0"
    else:
        pad = "1"
    newout = flash(IN, pad)
    IN = newout

print(count(newout))
