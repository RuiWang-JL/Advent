with open('day2.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]

def part1():
    count = 0
    for line in lines:
        x,y,password = line.split()
        low, high = [int(ele) for ele in x.split('-')]
        s = y[0:1]
        if low <= password.count(s) <= high: count += 1
    print('part1: {}'.format(count))

def part2():
    count = 0
    for line in lines:
        x,y,password = line.split()
        pos1, pos2 = [int(ele)-1 for ele in x.split('-')]
        s = y[0:1]
        if ((s == password[pos1]) + (s == password[pos2])) == 1: count += 1
    print('part2: {}'.format(count))

part2()