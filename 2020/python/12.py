import time
start_time = time.time()

with open('day12.txt') as f:
    lines = [x.strip() for x in f.readlines()]

dirs = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
rot = {'L': 1j, 'R': -1j}


def part1():
    pos = 0+0j
    face = 1+0j
    for line in lines:
        ins,step = line[0],int(line[1:])
        if ins in dirs:
            pos += dirs[ins] * step
        elif ins in rot:
            face *= rot[ins] ** (step/90)
        else:
            pos += face * step
    print(abs(pos.real)+abs(pos.imag))


def part2():
    ship = 0j
    wp = 10+1j
    for line in lines:
        ins,step = line[0],int(line[1:])
        if ins in dirs:
            wp += dirs[ins] * step
        elif ins in rot:
            wp *= rot[ins]**(step/90)
        else:
            ship += step*wp
    print(abs(ship.real)+abs(ship.imag))

part2()
print("--- %s seconds ---" % (time.time() - start_time))