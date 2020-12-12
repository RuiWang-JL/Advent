import numpy as np
import re
from collections import defaultdict

with open('day8.txt') as f:
    lines = [x.strip() for x in f.readlines()]

def run(lines):
    i = 0   
    acc_count = 0
    seq = []
    while i < len(lines):
        i = i%len(lines)
        if i in seq:
            return seq            
            break
        seq.append(i)
        inst = lines[i].split()[0]
        num = lines[i].split()[1]
        if inst == 'acc':
            acc_count = acc_count+int(num)
        if inst == 'jmp':
            i+=(int(num)-1)
        i+=1
        if i ==len(lines):
            print('Final count:'+str(acc_count))

seq = run(lines)

for j in seq:
    if lines[j].split()[0] == 'nop':
        lines[j] = lines[j].replace('nop', 'jmp')
        run(lines)
        lines[j] = lines[j].replace('jmp', 'nop')
    elif lines[j].split()[0] == 'jmp':
        lines[j] = lines[j].replace('jmp', 'nop')
        run(lines)
        lines[j] = lines[j].replace('nop', 'jmp')
