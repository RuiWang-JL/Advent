
with open('test.txt', 'r+') as f:
# with open('01.txt', 'r+') as f:
    tot = 0 
    alltot = []
    for line in f.readlines():
        if len(line) <4: 
            alltot.append(tot)
            tot =0 
        else: tot += int(line.strip())
alltot.sort()
print("part 1: {}".format(max(alltot)))
print("part 2: {}".format(alltot[-1]+ alltot[-2]+ alltot[-3]))
