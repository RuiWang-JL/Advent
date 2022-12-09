
from collections import defaultdict
 
# with open('test.txt', 'r+') as file:
with open('09.txt', 'r+') as file:
    lines = [line.strip() for line in file.readlines()]
lrope = 10
rope = [[0, 0] for z in range(lrope)]
tpos = defaultdict(int)
 
for line in lines:
    direction, steps = line.split()
    steps = int(steps)
    if(direction == 'R'):
        dd = (1, 0)
    if(direction == 'U'):
        dd = (0, -1)
    if(direction == 'D'):
        dd = (0, 1)
    if(direction == 'L'):
        dd = (-1, 0)
    for i in range(0, steps):
        rope[0][0] += dd[0]
        rope[0][1] += dd[1]
 
        # each knot follows 1
        # each knot follows 1,2,3,4,5,6,7,8,9
        for i in range(1, lrope):
            h = rope[i - 1]
            t = rope[i]
            # same x
            diffx = h[0]-t[0]
            diffy = h[1]-t[1]
            if(abs(diffx)==2 and diffy==0):
                if diffx >0:
                    t[0]+=1
                else:
                    t[0]-=1
            # same y
            elif(abs(diffy) == 2 and diffx==0):
                if diffy >0:
                    t[1]+=1
                else:
                    t[1]-=1
            # diag 
            elif(abs(diffx) + abs(diffy) > 2):
                if diffx >0:
                    t[0]+=1
                else:
                    t[0]-=1
                if diffy >0:
                    t[1]+=1
                else:
                    t[1]-=1
        tpos[(t[0], t[1])]+=1
 
print(len(tpos.keys()))