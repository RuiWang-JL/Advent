with open("08.txt", "r") as f:
# with open("test.txt", "r") as f:
    c = [[int(n) for n in l.strip()] for l in f.readlines()]
d = len(c)
tot = 0
lmul=[]

for x in range(1, d - 1):
    for y in range(1, d - 1):
        top = True
        down = True
        left = True
        right = True
        mul = 1
        test = []

        for i in range(x-1, -1, -1):
            if c[i][y] >= c[x][y]:
                mul*=(x-i)
                test.append((x-i, "top"))
                top = False
                break

        for i in range(x + 1, d):
            if c[i][y] >= c[x][y]:
                down = False
                mul*=(i-x)
                test.append((i-x, "down"))
                break

        for i in range(y-1, -1,-1):
            if c[x][i] >= c[x][y]:
                mul*=(y-i)
                right = False
                test.append((y-i, "left"))
                break

        for i in range(y + 1, d):
            if c[x][i] >= c[x][y]:
                mul*=(i-y)
                left = False
                test.append((i-y,"right"))
                break

        if left:mul*=(d-y-1)
        if right:mul*=(y)
        if top:mul*=(x)
        if down:mul*=(d-x-1)


        if top or down or left or right is True:
            tot+=1
        lmul.append(mul)

print(tot + 4 * d - 4)
print(max(lmul))