from collections import deque

# with open('test.txt', 'r+') as file:
with open('12.txt', 'r+') as file:
    grid = [list(line.strip()) for line in file.readlines()]
mx, my = len(grid[0]), len(grid)

notvis = deque()
dis = {}
for y in range(my):
    for x in range(mx):
        if grid[y][x] == 'S' or grid[y][x] =='a':
        # if grid[y][x] == 'S':
            notvis.append((x,y))
            dis[(x,y)]=0
            grid[y][x]=0
        elif grid[y][x]=="E":
            end = (x,y)
            grid[y][x]=25
        else:
            grid[y][x]= ord(grid[y][x]) - ord('a')

while True: 
    x,y = notvis.popleft()
    if (x,y)==end:
        break
    for dx, dy in ((1,0),(-1,0),(0,-1),(0,1)):
        xx = dx+x
        yy = dy+y
        if (0<=xx<mx and 0<=yy<my and (xx,yy) not in dis.keys() and grid[yy][xx]-grid[y][x]<=1 ):
            notvis.append((xx,yy))
            dis[(xx,yy)] = dis[(x,y)]+1
print(dis[end])
