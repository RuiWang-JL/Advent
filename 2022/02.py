
# with open('test.txt', 'r+') as f:
with open('02.txt', 'r+') as f:
    tot = 0
    for line in f.readlines():
        them = line.split()[0]
        me = line.split()[1]
        if them == "A":
            them = "X"
        elif them == "B":
            them = "Y"
        elif them == "C":
            them = "Z"
            
        if(them+me) == "XX":
            tot+= 3+0
        if(them+me) == "YX":
            tot+= (1+0)
        if(them+me) == "ZX":
            tot+= 2+0
        if(them+me) == "XY":
            tot+= (1+3)
        if(them+me) == "YY":
            tot+= 2+3
        if(them+me) == "ZY":
            tot+= 3+3
        if(them+me) == "XZ":
            tot+= 2+6
        if(them+me) == "YZ":
            tot+= 3+6
        if(them+me) == "ZZ":
            tot+= 1+6
        print(them+me)

    print(tot)