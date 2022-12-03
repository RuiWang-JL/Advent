# with open('test.txt', 'r+') as f:
with open('03.txt', 'r+') as f:
    tot = 0
    k,s,t = set(), set(), set()
    lines = [line.strip() for line in f.readlines()]
    for i, line in enumerate(lines):
        # first ,second = line[:len(line)//2], line[len(line)//2:]
        # k, s = set(first), set(second)
        if(i%3==0):
            com = k&s&t
            k = set(line)
        if(i%3==1):
            s = set(line)
        if(i%3==2):
            t = set(line)
        if(len(com)>0):
            m = com.pop()
            intm = ord(m)
            if(intm<97):
                tot+= (intm-64) + 26
            else:
                tot+= (intm-96)
print(tot)

