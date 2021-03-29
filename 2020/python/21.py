import time
import re
from collections import defaultdict
start_time = time.time()

with open('21.txt') as f:
    lines = [x.strip() for x in f.readlines()]

ingres = set()
allgs = set()
allg_line = defaultdict(set)
ingre_line = defaultdict(list)
ing_in_all = defaultdict(set)
bads = set()
for i, line in enumerate(lines):
    elems = line.replace(')', '').replace(',', '').split()
    after_c = False
    for ele in elems:
        if '(contains' in ele:
            after_c = True
        elif not after_c:
            ingres.add(ele)
            ingre_line[i].append(ele)
        elif after_c:
            allgs.add(ele)
            allg_line[ele].add(i)
for key in allg_line:
    ing_in_all[key] = list(set.intersection(*map(set, [ingre_line[i] for i in allg_line[key]])))
    for ele in ing_in_all[key]:
        bads.add(ele)
cnt = 0
for line in ingre_line.values():
    for ele in line:
        if ele not in bads:
            cnt +=1

print(bads)
def part1():
    #print(ingre_line,allg_line)
    print(cnt)

def part2():
    print(ing_in_all)
# dairy = lmcqt
# egg kcddk
# fish npxrdnd
# nuts cfb 
# penuts: ldkt
# seasame fqpt
# shellfish: jtfmtpd
# soy: tsch





part2()

print("--- %s seconds ---" % (time.time() - start_time))