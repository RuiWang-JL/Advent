with open('day1.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]

i = 0
counter = 0
while i < len(lines)-3:
    diff = int(lines[i+3]) - int(lines[i])
    i = i+1
    if diff > 0:
        counter = counter + 1

print(counter)
