from collections import defaultdict

x = [14,8,16,0,1]
dic = defaultdict(int)
t = 17

for pos,ele in enumerate(x):
    dic[ele] = pos

for pos in range(len(x),2020-1): 
    if t in dic.keys():
        nt = pos - dic[t]
    else:
        nt = 0
    
    dic[t] = pos            
    t = nt

print(t)

