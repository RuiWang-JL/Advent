import math
import copy
# with open('test.txt', 'r+') as file:
with open('11.txt', 'r+') as file:
    lines = [line.strip() for line in file.readlines()]
n_monkey = 8
monkeys =[]
m =[]
ops = []
v = []
test = []
iftrue = []
iffalse = []
tot = 0
times=[0 for ele in range(n_monkey)]
for i,line in enumerate(lines):
    if i%7==0:
        m.clear()        
    if i%7==1:
        nl = line[16:]
        items = [int(e) for e in nl.split(', ')]
        monkeys.append(items)
    if i%7 == 2:
        op = line[21:22]
        ops.append(op)
        if line[23:].isnumeric():
            v.append(int(line[23:]))
        else:
            v.append(0)

    if i%7==3:
        test.append(int(line.split()[3]))
    if i%7==4:
        iftrue.append(int(line.split()[5]))
    if i%7==5:
        iffalse.append(int(line.split()[5]))

# print(monkeys,ops,v, test,iftrue,iffalse)
# print(test)
# for rui in range(1000, 1010):
mo = 1
for i in test:
    mo*=i
for k in range(10000):
    for i in range(n_monkey):
        mon = monkeys[i]
        oldmon = copy.deepcopy(mon)
        for s in range(len(oldmon)):
            wl = oldmon[s]
            op = ops[i]
            if v[i] == 0:
                v2 = wl
            else:
                v2 = v[i]
        
            if op == '*':
                wl *=v2 
            if op == '+':
                wl +=v2 
            # get bored
            wl = wl % mo
            if wl % test[i] == 0:
                monkeys[iftrue[i]].append(wl)
            else:
                monkeys[iffalse[i]].append(wl)
            mon.clear()
            times[i]+=1
times.sort()
print(times[-1]*times[-2])
