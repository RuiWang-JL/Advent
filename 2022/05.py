# import numpy as np
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# [C]         [S] [H]                
# [F] [B]     [C] [S]     [W]        
# [B] [W]     [W] [M] [S] [B]        
# [L] [H] [G] [L] [P] [F] [Q]        
# [D] [P] [J] [F] [T] [G] [M] [T]    
# [P] [G] [B] [N] [L] [W] [P] [W] [R]
# [Z] [V] [W] [J] [J] [C] [T] [S] [C]
# [S] [N] [F] [G] [W] [B] [H] [F] [N]
#  1   2   3   4   5   6   7   8   9 
# with open('test.txt', 'r+') as f:
with open('05.txt', 'r+') as f:
    # l0= ["Z", "N"]
    # l1= ["M", "C", "D"]
    # l2= ["P"]
    biglist = [list("szpdlbfc"),
               list("nvgphwb"),
               list("fwbjg"),
               list("gjnflwcs"),
               list("wjltpmsh"),
               list("bcwgfs"),
               list("htpmqbw"),
               list("fswt"),
               list("ncr"),
               ]
    tot = 0
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        _,a,_, b,_,c = line.split()
        a,b,c = int(a),int(b)-1,int(c)-1
        diff=[]
        for i in range(a):
            k = biglist[b].pop() 
            diff.append(k)
        for i in range(a):
            k=diff.pop()
            biglist[c].append(k)
    for ele in biglist:
        print(ele[-1])



