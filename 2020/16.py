import time
import re
from collections import defaultdict
start_time = time.time()

with open('day16.txt') as f:
    lines = [x.strip() for x in f.readlines()]
def part1():
    #extract rules
    rules = []
    tot = 0
    for i in range(20):
        rule=[]
        for ele in re.findall('[0-9]+',lines[i]):
            rule.append(int(ele))
        rules.append(rule) 
    
    for i in range(25,260):
        for ele in re.findall('[0-9]+',lines[i]):
            belong = False
            for rule in rules:
                if rule[0]<= int(ele) <= rule[1] or rule[2]<= int(ele) <= rule[3]:
                    belong = True
                    break
            if belong == False:
                tot +=int(ele)
    print(tot)

def part2():
    #extract rules
    rules = {}
    tot = 0
    valids = []

    yours = lines[22].split(',')

    for i in range(20):
        rule=[]
        for ele in re.findall('[0-9]+',lines[i]):
            rule.append(int(ele))
        rules[lines[i].split(':')[0]] = rule
    
    for i in range(25,260):
        valid = True
        for ele in re.findall('[0-9]+',lines[i]):
            belong = False
            for rule in rules.keys():
                if rules[rule][0]<= int(ele) <= rules[rule][1] or rules[rule][2]<= int(ele) <= rules[rule][3]:
                    belong = True
                    break
            if belong == False:
                tot +=int(ele)
                valid = False
                break
        if valid:
            valids.append(list(lines[i].split(',')))
    
    srules = defaultdict(set)
    
    for i in range(20): # Each number in a ticket
        for rule in rules.keys(): # Check if all tickets for that number belong to one key
            belongToRule = True
            for row in valids: # Check all tickets for that number int(row[i])
                if rules[rule][0]<= int(row[i]) <= rules[rule][1] or rules[rule][2]<= int(row[i]) <= rules[rule][3]:
                    belongToRule = True
                else:
                    belongToRule = False
                    break
            if belongToRule == True:
                srules[rule].add(i)
    a = sorted(srules.items(), key=lambda x: len(x[1]))  

    taken = set()
    nrules = {}
    for ele in a:
        for x in ele[1]:
            if x not in taken:
                nrules[ele[0]] = x
                taken.add(x)
                break
    ans = 1
    for ele in nrules.items():
        if 'departure' in ele[0]:
            ans *= int(yours[ele[1]]) 
    print(ans)

part2()

print("--- %s seconds ---" % (time.time() - start_time))