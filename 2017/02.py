from itertools import permutations
# with open('test.txt', 'r+') as f:
with open('02.txt', 'r+') as f:
    tot = 0
    for line in f.readlines():
        int_line = [int(x) for x in line.split()]
        combos = (list(permutations(int_line, 2)))
        for x,y in combos:
            if x%y == 0:
                diff=x/y
        # diff = max(int_line) - min(int_line)
                tot+=diff

print(tot)
