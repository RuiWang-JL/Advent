import math
with open('day16.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
input = lines[0]
b = bin(int(input, 16))[2:]
versiontot = 0


def decode(index):
    global versiontot
    version, type = b[index:3+index], b[3+index:6+index]  # 3bits +3bits
    index += 6
    versiontot += int(version, 2)
    vals = []
    if type == "100":
        val = ""
        while True:
            index += 5
            val += b[index-4:index]  # index 7,8,9,10
            if b[index-5] == "0":
                # find the last 0
                break
        val = int(val, 2)
        return index, val
    else:
        lengthid = b[index]
        if lengthid == "0":
            L = int(b[1+index:16+index], 2)
            endi = index + 16+L
            index += 16
            while index < endi:
                index, val = decode(index)
                vals.append(val)
        else:
            N = int(b[1+index:12+index], 2)
            index += 12
            for _ in range(N):
                index, val = decode(index)
                vals.append(val)
    if type == "000":
        val = sum(vals)
    if type == "001":
        val = math.prod(vals)
    if type == "111":
        if vals[0] == vals[1]:
            val = 1
        else:
            val = 0
    if type == "010":
        val = min(vals)
    if type == "011":
        val = max(vals)
    if type == "101":
        if vals[0] > vals[1]:
            val = 1
        else:
            val = 0
    if type == "110":
        if vals[0] < vals[1]:
            val = 1
        else:
            val = 0
    return index, val


_, val = decode(0)
print(versiontot)
print(val)
