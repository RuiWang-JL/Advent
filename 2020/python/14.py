import time
from collections import defaultdict
import re
import copy

start_time = time.time()

with open('day14.txt') as f:
    lines = [x.strip() for x in f.readlines()]


def part1():
    tot = 0
    mem = defaultdict(int)
    for line in lines:
        if 'mask' in line:
            mask = line[7:]
        else:
            pos,v = [int(ele) for ele in re.findall('[0-9]+',line)]
            binv = bin(v)[2:]

            for i in range(len(binv),36):
                binv = '0'+ binv
            
            binv = list(binv)
            for i in range(36):
                if mask[i]!='X':
                    binv[i]=mask[i]
            strbinv = ''.join(binv)
            mem[pos] = strbinv
    for ele in mem.values():
        tot = tot + int(ele,2)
    print(tot)

def part2():
    tot = 0
    npos = []
    mem = defaultdict(int)
    for line in lines:
        if 'mask' in line:
            mask = line[7:]
        else:
            xs=[]
            pos,v = [int(ele) for ele in re.findall('[0-9]+',line)]
            bpos = bin(pos)[2:]

            for i in range(len(bpos),36):
                bpos = '0'+ bpos
            
            bpos = list(bpos)
            for i in range(36):
                if mask[i]!='X':
                    bpos[i]= str(int(mask[i]) or int(bpos[i]))
                else:
                    xs.append(i)
            for i in range(2**len(xs)):
                j = bin(i)[2:]
                j= j.zfill(len(xs))

                new = ['0']*36
                for i, ele in enumerate(xs):
                    new[ele]=j[i]

                n= copy.deepcopy(bpos)
                for i in xs:
                    n[i] = new[i]
                newn = ''.join(n)
                mem[newn] = v
    for ele in mem.values():
        tot = tot + ele
    print(tot)
part2()

print("--- %s seconds ---" % (time.time() - start_time))