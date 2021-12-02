with open('day2.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]

x = 0
y = 0
aim = 0
for line in lines:
    a, b = line.split()
    if a == "forward":
        x = x + int(b)
        y = y + aim*int(b)
    elif a == "down":
        aim = aim + int(b)
    elif a == "up":
        aim = aim - int(b)
print(x*y)
