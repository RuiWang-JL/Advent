import sys, os

bpass = []

with open('day5.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
    
    for line in lines:
        newline = line.replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1')
        bpass.append(int(newline,2))
    
    print(max(bpass))
    myseat = [print(seat) for seat in range(min(bpass),max(bpass)) if not seat in bpass]

