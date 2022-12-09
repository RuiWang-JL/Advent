
# with open('test.txt', 'r+') as file:
with open('05.txt', 'r+') as file:
    tot = 0
    lines = [int(line.strip()) for line in file.readlines()]
    kmax= len(lines)
    i = 0
    li = [0]
    s =0
    while(i<kmax):
        # ci  0, 0, 1
        # i 0, 1, 4, 
        li.append(i)
        s+=1
        jump = lines[i]
        i+=jump
        
        if i < kmax:
            if jump>2:
                lines[li[s]]-=1
            else:    
                lines[li[s]]+=1
print(s)