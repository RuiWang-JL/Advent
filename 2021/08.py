with open('day8.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]


def setdiff(longn, shn):
    return (set(longn) - set(shn))


tot = 0
digits = {}
j = {}
res = 0
for line in lines:
    a = line.split('|')[1].split()
    b = line.split('|')[0].split()
    for num in b:
        sorted_num = sorted(b, key=len)
        ss = [set([char for char in ele]) for ele in sorted_num]
        digits["1"] = ss[0]
        digits["7"] = ss[1]
        digits["4"] = ss[2]
        digits["8"] = ss[9]
        j["b,d"] = setdiff(ss[2], ss[0])
        j["2,3,5"] = [ss[3], ss[4], ss[5]]
        j["6,9,0"] = [ss[6], ss[7], ss[8]]
        for ele in j["2,3,5"]:
            if j["b,d"].issubset(ele):
                digits["5"] = ele
        j["c,e"] = setdiff(ss[9], digits["5"])
        for ele in j["6,9,0"]:
            if not digits["7"].issubset(ele):
                digits["6"] = ele
        j["c"] = setdiff(ss[9], digits["6"])
        j["e"] = setdiff(j["c,e"], j["c"])
        for ele in j["6,9,0"]:
            if not j["e"].issubset(ele):
                digits["9"] = ele
        for ele in j["6,9,0"]:
            if not ele in [digits["9"], digits["6"]]:
                digits["0"] = ele
        for ele in j["2,3,5"]:
            if digits["1"].issubset(ele):
                digits["3"] = ele
        for ele in j["2,3,5"]:
            if not ele in [digits["5"], digits["3"]]:
                digits["2"] = ele
    dig = []
    for ele in a:
        for key, v in digits.items():
            if set(ele) == v:
                dig.append(int(key))
    tot = 1000*dig[0]+100*dig[1]+10*dig[2]+dig[3]
    res += tot
print(res)
