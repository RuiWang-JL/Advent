from collections import defaultdict

path = []
sizes = defaultdict(int)
tot=0
# with open('test.txt', 'r+') as file:
with open('07.txt', 'r+') as file:
    lines = [line.strip() for line in file.readlines()]
    for l in lines:
        l = l.split()
        if l[0] == '$':
            if l[1] == 'cd':
                if l[2] == '/':
                    path = []
                elif l[2] == '..':
                    path.pop()
                else:
                    path.append(l[2])
        # end of branch
        # all path in the parent branch will add the value
        if l[0].isdigit():
            for i in range(len(path)+1):
                pwd = '/'+'/'.join(path[:i])
                sizes[pwd] += int(l[0])
    big =[]
    for v in sizes.values():
        if v<=100000:
            tot+=v
        if v>=sizes['/'] - 40000000:
            big.append(v)
    big.sort()
    print(big[0])


print(tot)





