
with open('day22.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
nl = []
xyzs = []
for line in lines:
    ins, cords = line.split()
    x, y, z = cords.split(",")
    x = x[2:]
    x1, x2 = x.split("..")
    x1 = int(x1)
    x2 = int(x2)
    y = y[2:]
    y1, y2 = y.split("..")
    y1 = int(y1)
    y2 = int(y2)
    z = z[2:]
    z1, z2 = z.split("..")
    z1 = int(z1)
    z2 = int(z2)
    nl.append((ins, (x1, x2, y1, y2, z1, z2)))
    xyzs.append((x1, x2, y1, y2, z1, z2))


def overlap(cub1, cub2):
    x1, x2, y1, y2, z1, z2 = cub1
    xx1, xx2, yy1, yy2, zz1, zz2 = cub2
    if xx1 < x2 and xx2 > x1 and yy1 < y2 and yy2 > y1 and zz1 < z2 and zz2 > z1:
        x = [xx1, xx2, x1, x2]
        x.sort()
        y = [yy1, yy2, y1, y2]
        y.sort()
        z = [zz1, zz2, z1, z2]
        z.sort()
        return (x[1], x[2], y[1], y[2], z[1], z[2])
    return False


oncubs = []
offcubs = []


def onoff(oncubs, offcubs):
    toton = 0
    totoff = 0
    for cub in oncubs:
        x1, x2, y1, y2, z1, z2 = cub
        toton += (x2-x1+1)*(y2-y1+1)*(z2-z1+1)

    for cub in offcubs:
        x1, x2, y1, y2, z1, z2 = cub
        totoff += (x2-x1+1)*(y2-y1+1)*(z2-z1+1)
    # print(toton-totoff)
    return toton-totoff


for ins, cub in nl:  # add cub
    newoff = []
    newon = []
    if ins == "on":
        for on in oncubs:
            if overlap(on, cub):
                overlapcub = overlap(on, cub)
                newoff.append(overlapcub)
        oncubs.append(cub)
        for off in offcubs:
            if overlap(off, cub):
                overlapcub = overlap(off, cub)
                oncubs.append(overlapcub)
        offcubs += newoff
    if ins == "off":
        for on in oncubs:
            if overlap(on, cub):
                overlapcub = overlap(on, cub)
                newoff.append(overlapcub)
        for off in offcubs:
            if overlap(off, cub):
                overlapcub = overlap(off, cub)
                oncubs.append(overlapcub)
        offcubs += newoff
print(onoff(oncubs, offcubs))
