import re
from  itertools import product
from collections import defaultdict
import time
start_time = time.time()
with open('19.txt') as f:
    lines = [x.strip() for x in f.readlines()]

rules = lines[0:136] # 136
rules.sort(key=lambda e : int(re.search("[0-9]+:",e).group(0)[0:-1]))
dict_r = defaultdict(list)
data = lines[137:578] # 137:578

abrule = defaultdict(list)
abrule[30] = ["a"]
abrule[20] = ["b"]

for i, line in enumerate(rules):
    dict_r[i] = [[int(p) for p in k.split(" ") if p.isnumeric()] for k in line.split(":")[1].split("|")]


def find(x):
    if abrule[x]!=[]:return abrule[x]
    for pairs in dict_r[x]:
        new = []
        for i in pairs:
            new += [find(i)]
        abrule[x] += ["".join(pairs for pairs in list(y)) for y in product(*new)]
        #print(new)
        #print(new, 'find{}'.format(x))
    return abrule[x]

def part1():
    find(11)
    r0 = set(abrule[0])
    print(set(abrule[11]))
    tot = 0
    #for line in data:
    #     if line in r0:
    #         tot += 1
   
    # for i in r0:
    #     for ele in data:
    #         if i in ele:
    #             tot +=1
    #             break
    # print(tot)
part1()


print("--- %s seconds ---" % (time.time() - start_time))
