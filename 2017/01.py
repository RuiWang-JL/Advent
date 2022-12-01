# with open('test.txt', 'r+') as f:
with open('01.txt', 'r+') as f:
    line_str = f.readline()
    line = [int(x) for x in line_str]

def part(x):
    tot = 0
    for i in range(len(line)):
        if line[i] == line[i-x]:
            tot +=line[i]
    return tot

print('part1:{} '.format(part(1)))
print('part1:{} '.format(part(int(len(line)/2))))
