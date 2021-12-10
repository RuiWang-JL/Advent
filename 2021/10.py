import numpy as np
with open('day10.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
left = "[({<"
right = "])}>"
pairs = {"]": "[", "}": "{", ")": "(", ">": "<"}


def findpair(line):
    k = []
    tot = 0
    for ele in line:
        # print(ele)
        if ele in left:
            k.append(ele)
        elif ele in right:
            if pairs[ele] == k[-1]:
                if len(k) > 0:
                    k.pop()
            else:
                return
    # print(k)
    if len(k) > 0:
        k.reverse()
    # print(k)
    for res in k:
        if res == "(":
            tot = tot*5 + 1
        elif res == "[":
            tot = tot*5 + 2
        elif res == "{":
            tot = tot*5 + 3
        elif res == "<":
            tot = tot*5 + 4
    return tot


n = []
for line in lines:
    res = findpair(line)
    if res:
        n.append(res)
# print(n)
n.sort()
print(n[int(len(n)/2)])
#     if res == ")":
#         tot += 3
#     elif res == "]":
#         tot += 57
#     elif res == "}":
#         tot += 1197
#     elif res == ">":
#         tot += 25137
# print(tot)
# print(lines)
