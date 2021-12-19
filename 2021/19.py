from collections import defaultdict
from itertools import combinations
with open('day19.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
scanindex = 0
k = defaultdict(list)
for line in lines:
    if "---" in line:
        scanner = []
    if "," in line:
        ele3 = [int(ele) for ele in line.split(",")]
        scanner.append(ele3)
    if len(line) < 2:
        k[scanindex] = scanner
        scanindex += 1
# compare(sa, sb)
# rotate sa => 24 different ones
sh = [(0, 1, 2), (0, 2, 1), (1, 0, 2),
      (1, 2, 0), (2, 0, 1), (2, 1, 0)]
r = [(1, 1, 1), (1, -1, 1), (-1, 1, 1), (1, 1, -1),
     (-1, -1, 1), (-1, 1, -1), (1, -1, -1), (-1, -1, -1)]
# 48 different results

distances = [(0, 0, 0)]


def rotate(sb, shift, rot):
    rb = []
    for xline in sb:
        rb.append([rot[0]*xline[shift[0]], rot[1] *
                   xline[shift[1]], rot[2]*xline[shift[2]]])
    return rb


def check(sa, sb):
    sa_poses = set([tuple(x) for x in sa])
    for shift in sh:
        for rot in r:
            nb = rotate(sb, shift, rot)
            for a_pos in sa:
                for b_pos in nb:
                    s_diff = [(b_pos[0]-a_pos[0]), (b_pos[1] -
                                                    a_pos[1]), (b_pos[2]-a_pos[2])]
                    matches = 0
                    remapped = []
                    for b_pos2 in nb:
                        bpos_remap = (
                            b_pos2[0]-s_diff[0], b_pos2[1]-s_diff[1], b_pos2[2]-s_diff[2])
                        if bpos_remap in sa_poses:
                            matches += 1
                        remapped.append(list(bpos_remap))
                    if matches >= 12:
                        print("match", s_diff)
                        distances.append(s_diff)
                        return True, remapped
    return False, None


remaps = {}
remaps[0] = k[0]
knownidex = {0}
beacons = []
beacons = set([tuple(x) for x in k[0]])

while len(knownidex) < scanindex:
    for checking in range(scanindex+1):
        if checking in knownidex:
            continue
        for against in knownidex:
            print("checking", checking, "against", against)
            morethan12, remap = check(remaps[against], k[checking])
            if morethan12:
                knownidex.add(checking)
                remaps[checking] = remap
                beacons.update(set([tuple(x) for x in remap]))
                print(len(knownidex))
                break
print("part1", len(beacons))

mah = []
dis2 = combinations(distances, 2)
for a, b in list(dis2):
    mah.append(sum([abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2])]))
print(max(mah))
