with open('day13.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]

cor = set()
ins = []
for ele in lines:
    if "," in ele:
        x, y = ele.split(",")
        cor.add((int(x), int(y)))
    if "along" in ele:
        ins.append(ele.split()[2])


def up(x, cor):
    newcor = set()
    for ele in cor:
        if ele[0] > x:
            newcor.add((2*x-ele[0], ele[1]))
        elif ele[0] == x:
            continue
        else:
            newcor.add(ele)
    return newcor


def left(y, cor):
    newcor = set()
    first = 0
    second = 0
    for ele in cor:
        if ele[1] > y:
            newcor.add((ele[0], 2*y-ele[1]))
            first += 1
        elif ele[1] == y:
            continue
        else:
            second += 1
            newcor.add(ele)
    return newcor


for instruction in ins:
    if instruction[0] == "y":
        cor = left(int(instruction[2:]), cor)
    else:
        cor = up(int(instruction[2:]), cor)

p = '\n'
for y in range(10):
    for x in range(40):
        if (x, y) in cor:
            p += '#'
        else:
            p += ' '
    p += '\n'

print(p)
