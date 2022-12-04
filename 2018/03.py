tot=0
# with open('test.txt', 'r+') as f:
with open('03.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
    la = set()
    ldup = set()
    for line in lines:
        idnum, a = line.split("@")
        b, c = a.split(": ")
        aa, bb = b.split(",")
        cc, dd = c.split("x")
        aa = int(aa)
        bb = int(bb)
        cc, dd = int(cc) , int(dd)
        tot = cc*dd
        for x in range (cc):
            for y in range(dd):
                if (aa+x, bb+y) not in ldup:
                    if (aa+x, bb+y) not in la:
                        la.add((aa+x, bb+y))
                        tot-=1
                    else:
                        ldup.add((aa+x, bb+y))
        
    for line in lines:
        idnum, a = line.split("@")
        b, c = a.split(": ")
        aa, bb = b.split(",")
        cc, dd = c.split("x")
        aa = int(aa)
        bb = int(bb)
        cc, dd = int(cc) , int(dd)
        tot = cc*dd
        for x in range (cc):
            for y in range(dd):
                if(aa+x,bb+y) not in ldup:
                    tot-=1
        if tot ==0:
            print(idnum)
