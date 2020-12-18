from  itertools import product
import time
import re
from collections import defaultdict,deque

start_time = time.time()

with open('18.txt') as f:
    lines = [(x.strip().replace(' ', '')) for x in f.readlines()]

def no_brac(line):
    op = defaultdict(str)
    prev = defaultdict(str)
    level = 0
    for ele in line:
        # store the first number in prev when there is no operation
        # part1 method
        if ele.isnumeric() and op[level] == '':
            prev[level] = ele 
        elif ele.isnumeric():
            prev[level] = str(eval(prev[level]+op[level]+ele))
        elif ele == '*':
            op[level] = '*'
        elif ele == '+':
            op[level] = '+'
        elif ele == '(':
            level+=1 
        elif ele == ')':
            level-=1
            # part1 method
            if op[level] == '':
                prev[level] = prev[level+1]
            else:
                prev[level] = str(eval(prev[level]+op[level]+prev[level+1]))
            # clear the deeper level
            prev[level+1] = ''
            op[level+1] = ''
    return(prev[0])

def swape_order(line):
    a = defaultdict(list)
    tot = defaultdict(str)
    level = 0
    for ele in line:
        if ele == '(':
            level+=1 
        elif ele == ')':
            start = set()
            end = set()
            bracket_cnt = 0
            new = a[level][:]
            #print(a[level])
            for i,x in enumerate(a[level]):
                # No new open bracket
                if len(start) == len(end):
                    if x == '+':
                        bracket_cnt+=1
                        start.add(i-1)
                        
                        new.insert(i-1 + bracket_cnt-1,'(')         
                elif len(start) > len(end):
                    if x == '*':
                        end.add(i)
                        bracket_cnt+=1
                        new.insert(i + bracket_cnt-1,')')
            if len(start) > len(end):
                new.append(')')  
            newstr = ''.join(new)
            tot[level] = str(eval(newstr))
            level-=1
            a[level].append(tot[level+1])
            a[level+1] = []
            tot[level] = ''
        else:
            a[level].append(ele)
    start = set()
    end = set()
    bracket_cnt = 0
    new = a[0][:]
    #print(a[level])
    for i,x in enumerate(a[0]):
        # No new open bracket
        if len(start) == len(end):
            if x == '+':
                bracket_cnt+=1
                start.add(i-1)
                
                new.insert(i-1 + bracket_cnt-1,'(')         
        elif len(start) > len(end):
            if x == '*':
                end.add(i)
                bracket_cnt+=1
                new.insert(i + bracket_cnt-1,')')
    if len(start) > len(end):
        new.append(')')  
    newstr = ''.join(new)
    tot[0] = str(eval(newstr))
 
    return tot[0]

def part1():
    tot = 0
    for line in lines:
        #cal = no_brac(line)
        #print(line)
        cal = swape_order(line)
        tot += int(cal)
    print(tot)

part1()

print("--- %s seconds ---" % (time.time() - start_time))
