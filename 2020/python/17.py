from  itertools import product
import time

start_time = time.time()

with open('17.txt') as f:
    lines = [list(x.strip()) for x in f.readlines()]

def part1():
    active = set()
    for i,j in product(range(len(lines)),range(len(lines[0]))):
        if lines[i][j] == '#':
            active.add((i, j, 0, 0))
    for _ in range(6):
        new = set()
        new_ranges = product(
            range(min([elem[0] for elem in active])-1, max([elem[0] for elem in active])+2),
            range(min([elem[1] for elem in active])-1, max([elem[1] for elem in active])+2), 
            range(min([elem[2] for elem in active])-1, max([elem[2] for elem in active])+2), 
            range(min([elem[3] for elem in active])-1, max([elem[3] for elem in active])+2) 
        )
        for xx, yy, zz, ww in new_ranges:
            n = 0
            for x,y,z,w in product(range(xx-1,xx+2),range(yy-1,yy+2),range(zz-1,zz+2),range(ww-1,ww+2)):
                if (x,y,z,w) == (xx,yy,zz,ww):continue
                elif (x,y,z,w) in active:
                    n += 1
            if (
                (xx,yy,zz,ww) in active and 2 <= n <= 3 or 
                (xx,yy,zz,ww) not in active and n == 3
            ):
                new.add((xx,yy,zz,ww))
        active = new
    print(len(active))

part1()

print("--- %s seconds ---" % (time.time() - start_time))
