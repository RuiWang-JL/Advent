import re
from  itertools import product
from collections import defaultdict,deque
import time
start_time = time.time()


def move(cups,p):
    cl = len(cups)
    ncups = cups.copy() + cups.copy()
    c = ncups[p]
    pickup = ncups[p+1:p+4]
    ncups.pop((p+1)%cl)
    ncups.pop((p+1)%cl)
    ncups.pop((p+1)%cl)
    des = c - 1
    if des <=0:
        des = cl
    if des in pickup:
        while des in pickup:
            des = des - 1
            if des <= 0:
                des = cl

    if p ==cl-1:
        nn = ncups[p+1:p+cl-2]
    else:
        nn = ncups[p:p+cl-3]
    index = nn.index(des)
    nnn = nn[0:index+1] + pickup + nn[index+1:]
    nd = deque(nnn)
    if p == cl-1:
        nd.rotate(p+1)
    else:
        nd.rotate(p)
    return list(nd)


def part1():
    #cups = [3,6,2,9,8,1,7,5,4]
    cups = [3,8,9,1,2,5,4,6,7]
    # for x in range(10,1000001):
    #     cups.append(x)
    

    # for i in range(0,10000000):
    #     cups = move(cups,i%9)
    print(cups)
part1()


print("--- %s seconds ---" % (time.time() - start_time))
