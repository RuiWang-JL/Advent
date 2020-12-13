import time
from functools import reduce

start_time = time.time()

with open('day13.txt') as f:
    lines = [x.strip() for x in f.readlines()]


def part1():
    start = int(lines[0])
    buses = [int(ele) for ele in lines[1].split(',') if ele != 'x']
    times = [(bus-start%bus) for bus in buses]
    mint = min(times)  
    print(times)
    for i, time in enumerate(times):
        if time == mint:
            print(buses[i]*times[i])

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def part2():
    times=[]
    buses = [ele for ele in lines[1].split(',') if ele != 'x']
    for i, bus in enumerate(lines[1].split(',')):
        if bus in buses:
            times.append(-i)
    int_buses = [int(ele) for ele in buses]
    print(int_buses,times)
    print(chinese_remainder(int_buses, times))

part2()

print("--- %s seconds ---" % (time.time() - start_time))