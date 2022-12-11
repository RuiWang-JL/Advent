
# with open('test.txt', 'r+') as file:
with open('10.txt', 'r+') as file:
    lines = [line.strip() for line in file.readlines()]
cycle=0
x=1
tot=0

def func(cycle, tot, head):
    cycle+=1
    # if cycle % 40 == 20:
        # print(cycle, x, cycle*x)
        # tot+=x*cycle
    # 
    # print("cycle:",cycle, "draw pos",cycle%40-1,"head:",head, "diff:",abs(head-cycle%40))
    if abs(head-(cycle%40-1))<2:
        nl.append("#")
    else:
        nl.append(" ")
    if cycle % 40 == 0:
        print(''.join(nl))
        nl.clear()
    return cycle,tot


nl = []
for i,line in enumerate(lines):
    if line[0]=='a':
        step = int(line.split()[1])
        cycle,tot = func(cycle,tot,x)
        cycle,tot = func(cycle,tot,x)
        x+=step
    else:
        cycle,tot = func(cycle,tot,x)
            
# print(tot)