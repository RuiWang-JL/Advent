import math
from itertools import permutations
with open('day18.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]


def indexvv(line):
    index = 0
    newline = ""
    il = []
    freshdig = True
    for ele in line:
        if ele not in ("[", "]"):
            newline += ele
    newints = [int(ele) for ele in newline.split(",")]
    for ele in line:
        if ele == "[":
            index += 1
        elif ele == "]":
            index -= 1
        elif ele == ",":
            freshdig = True
        elif ele.isdigit() and freshdig:
            il.append((index, newints.pop(0)))
            freshdig = False
    return il


def explode(resultline):
    newline = []
    exploded = False
    finishedfirst = False
    needtoadd = False
    for index, value in resultline:
        if index < 5 or exploded:
            if needtoadd:
                newline.append((index, value+storevalue))
                needtoadd = False
            else:
                newline.append((index, value))
        else:
            if finishedfirst:
                storevalue = value
                exploded = True
                needtoadd = True
            else:
                if len(newline) > 0:
                    nindex, nvalue = newline[-1]
                    newlast = nindex, nvalue+value
                    newline[-1] = newlast
                    newline.append((4, 0))
                elif len(newline) == 0:
                    newline.append((4, 0))
                finishedfirst = True
    return newline


def findfirstgreater10(resultline):
    for _, value in resultline:
        if value >= 10:
            return True
    return False


def findfirstindex(resultline, i):
    for index, _ in resultline:
        if index >= i:
            return True
    return False


def splitfirst(resultline):
    newline = []
    splited = False
    for index, value in resultline:
        if value < 10 or splited:
            newline.append((index, value))
        else:
            first = math.floor(value/2)
            second = math.ceil(value/2)
            newline.append((index+1, first))
            newline.append((index+1, second))
            splited = True
    return newline


def calculatefirst(resultline, i):
    newline = []
    totfind = 0
    tot = 0
    for index, value in resultline:
        if index == i and totfind == 0:
            totfind += 1
            tot += value*3
        elif index == i and totfind == 1:
            totfind += 1
            tot += value*2
            newline.append((i-1, tot))
        else:
            newline.append((index, value))
    return newline


def sumres(lines):
    for i, line in enumerate(lines):
        nline = indexvv(line)  # [(4,0), (4,13)]
        resultline = []
        if i == 0:
            lastline = nline
        else:
            # addiction
            for index, value in lastline:
                resultline.append((index+1, value))
            for index, value in nline:
                resultline.append((index+1, value))
            # if there are index5
            while findfirstindex(resultline, 5):
                resultline = explode(resultline)
            # while there is greaterequal10
            while findfirstgreater10(resultline):
                resultline = splitfirst(resultline)
                resultline = explode(resultline)
            lastline = resultline
    return resultline


def mag(lastline):
    for i in range(4, 0, -1):
        while findfirstindex(lastline, i):
            lastline = calculatefirst(lastline, i)
    return lastline[0][1]


perm = permutations(lines, 2)
sumset = set()
for twolines in perm:
    sumline = sumres(twolines)
    m = mag(sumline)
    sumset.add(m)
print(max(sumset))
