import re
ds = []
ls = []
nb = set()
b = set()
ty = 2000000
# y = 10
s = []
# with open('test.txt', 'r+') as file:
with open('15.txt', 'r+') as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        sx,sy,bx,by = [int(s) for s in re.findall(r'\d+', line)]
        d = abs(sx -bx)+ abs(sy-by)
        dy = abs(ty-sy)
        ds.append(d)
        ls.append((sx,sy,bx,by))
        # if beacon distance is smaller than pure y axis distance, discard
        # when beacon distance is bigger than pure y asix distance
        # d is 5, dy is 3
        # part1
#         if dy <= d:
#             for i in range(dy-d+sx, d-dy+sx):
#                 nb.add(i)
# print(len(nb))
        # part 2

my=4000000
# my = 20
found=False
for y in range(my):
    bds=[]
    for i in range(len(ls)):
        sx,sy,bx,by=ls[i]
        d = ds[i]
        dy=abs(y-sy)
        if dy<=d:
            bds.append([max(0,sx-(d-dy)),min(sx+(d-dy),my)])
    bds=sorted(bds)
    cm=bds[0][1]
    for i in range(len(bds)-1):
        cm=max(cm,bds[i][1])
        if cm+1<bds[i+1][0]:
            print(4000000*(bds[i][1]+1)+y)
            found=True
    if found:
        break
