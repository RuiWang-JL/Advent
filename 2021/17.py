
# Xmin, Xmax = 20, 30
# Ymin, Ymax = -10, -5
Xmin, Xmax = 137, 171
Ymin, Ymax = -98, -73

# Vx, Vy = 6, 9
Vx, Vy = 17, 97
tot = 0
for initvx in range(Vx, Xmax+1):
    for initvy in range(Ymin, -Ymin):
        curvx = initvx
        curvy = initvy
        totx, toty = initvx, initvy
        while totx <= Xmax and toty >= Ymin:
            if Xmin <= totx <= Xmax and Ymin <= toty <= Ymax:
                tot += 1
                break

            if curvx > 0:
                curvx -= 1
            curvy -= 1
            totx += curvx
            toty += curvy
print(tot)
