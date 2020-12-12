import sys, os

num_needed = []

with open('day1.txt', 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        lines[i] = int(lines[i])
    for line in lines:
        if line < 1010:
            num_needed.append(2020-line)

    print(num_needed)

    for num in num_needed:
        if num in lines:
            print(num*(2020-num))
