# with open('test.txt', 'r+') as file:
with open('04.txt', 'r+') as file:
    tot = 0
    lines = [line.strip() for line in file.readlines()]
    # for l in lines:
    #     s = (set(l.split()))
    #     l = l.split()
    #     if len(l)== len(s):
    #         tot+=1
    for l in lines:
        nl = []
        for x in l.split():
            k = sorted(x)
            k = ''.join(k)
            nl.append(k)
        s = set(nl)
        if len(nl)== len(s):
            tot+=1
        
print(tot)
