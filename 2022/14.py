# with open('test.txt', 'r+') as file:
with open('14.txt', 'r+') as file:
    lines = [line.strip() for line in file.readlines()]
allone = []
oneset = set()
for line in lines:
    ll = line.split("->")
    one = []
    for lll in ll:
        p = lll.strip()
        a,b = [int(ele) for ele in p.split(',')]
        if len(one) == 0:
            oneset.add((a,b))
        else:
            olda, oldb = one[-1]
            if a == olda:
                for i in range(min(b,oldb), max(b,oldb)+1):
                    oneset.add((a, i))
            else:
                for i in range(min(a,olda), max(a,olda)+1):
                    oneset.add((i, b))
        one.append((a,b))
# fall off if drop goes too left or too right
xset = set()
yset = set()
for x,y in oneset:
    xset.add(x)
    yset.add(y)
for i in range(1000):
    oneset.add((i,max(yset)+2))
# drop from 500,0
fall = True
added = 0
while(fall):
    xs,ys = 500,0
    while True:
        if (xs, ys+1) not in oneset:
            ys+=1
        elif (xs-1, ys+1) not in oneset:
            xs-=1
            ys+=1
        elif (xs+1, ys+1) not in oneset:
            xs+=1
            ys+=1
        else:
            #come to rest

            # if xs >= max(xset)-1 or xs <= min(xset)+1:
            if xs == 500 and ys == 0:
                added+=1
                fall = False
                break
            added+=1
            oneset.add((xs,ys))
            break

print(len(oneset), max(xset), min(xset), max(yset), added)