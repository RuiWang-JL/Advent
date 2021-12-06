from collections import defaultdict
with open('day6.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
line = [int(ele) for ele in lines[0].split(',')]
ocean = defaultdict(int)
for ele in line:
    ocean[ele] += 1


def dayPass(ocean, day):
    newocean = defaultdict(int)
    for key, va in ocean.items():
        if key == 0:
            newocean[6] += ocean[0]
            if day > 1:
                newocean[8] += ocean[0]
        else:
            newocean[key-1] += ocean[key]
    return newocean


days = 256
for day in range(1, days+1):
    ocean = dayPass(ocean, day)

print(sum(ocean.values()))
