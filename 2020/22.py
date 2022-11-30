import time
import re
from collections import defaultdict, deque
from math import prod
start_time = time.time()

with open('22.txt') as f:
    ls = [x.strip() for x in f.readlines()]

p1 = deque()
p2 = deque()
pre = []
#player1
#crab
#for line in lines[1:6]: # 1:26
for line in lines[1:26]: # 1:26
    p1.append(int(line))
#print(p1)
#player2
#for line in lines[8:13]: # 1:26
for line in lines[28:53]: # 1:26
    p2.append(int(line))


def part1():
    tot = 0
    while len(p1) > 0 and len(p2) > 0:
        if p1[0]>p2[0]:
            p1.rotate(-1)
            p1.append(p2[0])
            p2.popleft()
        else:
            p2.rotate(-1)
            p2.append(p1[0])
            p1.popleft()
    if len(p1)>0:
        for i, ele in enumerate(p1):
            tot +=ele * (50-i)
        print(tot)
    else:
        for i, ele in enumerate(p2):
            tot +=ele * (50-i)
        print(tot)
    print(p1,p2)

def game(p1,p2):
    while len(p1) > 0 and len(p2) > 0:
        if (list(p1),list(p2)) not in pre or (list(p2),list(p1)) not in pre: 
            pre.append((list(p1),list(p2)))
        else:
            p1.rotate(-1)
            p1.append(p2[0])
            p2.popleft()
            continue
        if p1[0]<=len(p1)-1 and p2[0]<=len(p2)-1:
            pp1 = p1.copy()
            pp2 = p2.copy()
            r1 = pp1.popleft()
            r2 = pp2.popleft()
            if game(pp1,pp2):
                p1.rotate(-1)
                p1.append(p2[0])
                p2.popleft()
            else:
                p2.rotate(-1)
                p2.append(p1[0])
                p1.popleft()
        else:
            if p1[0]>p2[0] :
                p1.rotate(-1)
                p1.append(p2[0])
                p2.popleft()
            else:
                p2.rotate(-1)
                p2.append(p1[0])
                p1.popleft()
            
    if len(p1) > 0: return True
    else: return False 
        


def part2():
    tot = 0
    
    w1 = game(p1,p2)

    if w1:
        for i, ele in enumerate(p1):
            tot +=ele * (50-i)
            #tot +=ele * (10-i)
    else:
        for i, ele in enumerate(p2):
            tot +=ele * (50-i)
            #tot +=ele * (10-i)
    print(tot)
    print(p1,p2)
    print('part2')

part2()

# old_p1 = deque(map(int, ls[1:26]))
# old_p2 = deque(map(int, ls[28:]))


# def score(winner):
#     return sum(map(prod, enumerate(reversed(winner), 1)))


# # Part one
# p1 = deque(old_p1)
# p2 = deque(old_p2)

# while p1 and p2:
#     c1 = p1.popleft()
#     c2 = p2.popleft()
#     p1_won = c1 > c2
#     winner = p1 if c1 > c2 else p2
#     winner.append(c1 if p1_won else c2)
#     winner.append(c1 if not p1_won else c2)

# print(score(p1 or p2))


# # Part two
# def game(p1, p2):
#     seen = set()
#     while p1 and p2:
#         conf = (tuple(p1), tuple(p2))
#         if conf in seen:
#             return True, p1
#         seen.add(conf)
#         c1 = p1.popleft()
#         c2 = p2.popleft()
#         if len(p1) >= c1 and len(p2) >= c2:
#             p1_won, _ = game(deque(list(p1)[:c1]),
#                              deque(list(p2)[:c2]))
#         else:
#             p1_won = c1 > c2
#         winner = p1 if p1_won else p2
#         winner.append(c1 if p1_won else c2)
#         winner.append(c1 if not p1_won else c2)
#     return p1_won, winner


# _, winner = game(deque(old_p1), deque(old_p2))
# print(score(winner))

print("--- %s seconds ---" % (time.time() - start_time))