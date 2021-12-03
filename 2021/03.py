import copy
with open('day3.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]


def checkList(lines, checkbit):
    tot = 0
    for line in lines:
        linelinst = list(line)
        if linelinst[checkbit] == "1":
            tot += 1
    return tot >= len(lines)/2


def genNewList(lines, checkbit, reverse):
    res = checkList(lines, checkbit)
    newLines = []
    if reverse:
        res = not(res)
    for line in lines:
        if res and line[checkbit] == "1" or not(res) and line[checkbit] == "0":
            newLines.append(line)
    return newLines


def findLastOne(old, reverse):
    x = 0
    while len(old) > 1:
        temp = genNewList(old, x, reverse)
        old = copy.deepcopy(temp)
        x += 1
        if len(old) == 1:
            return int(old[0], 2)


print(findLastOne(lines, False) * findLastOne(lines, True))
