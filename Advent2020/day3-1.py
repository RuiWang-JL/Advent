import sys, os

twoDList = []
count2=0
count1=0
count3=0
count4=0
count5=0


with open('day3.txt', 'r+') as f:
    lines=f.readlines()
    for line in lines:
        line = list(line.strip())
        line.extend(line)
        line.extend(line)
        line.extend(line)
        line.extend(line)
        line.extend(line)
        line.extend(line)
        line.extend(line)
        twoDList.append(line)

row = len(twoDList)
columns = len(twoDList[0])

print(twoDList[0][3])
print(row, columns)

for x in range(0, row):
    if twoDList[x][3*x] is '#':
        count2 += 1

for x in range(0, row):
    if twoDList[x][x] is '#':
        count1 += 1
for x in range(0, row):
    if twoDList[x][5*x] is '#':
        count3 += 1

for x in range(0, row):
    if twoDList[x][7*x] is '#':
        count4 += 1

for x in range(0, row,2):
    if twoDList[x][x/2] is '#':
        count5 += 1

  
print(count1,count2, count3, count4, count5) 
print(count1*count2*count3*count4*count5)
