# with open('test.txt', 'r+') as f:
with open('04.txt', 'r+') as f:
    tot = 0
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        a, b = line.split(',')        
        a1, a2 = list(map(int, a.split('-')))
        b1, b2 = list(map(int, b.split('-')))
        lista = list(range(a1,a2+1))
        listb = list(range(b1,b2+1))
        # check =  all(item in lista for item in listb)
        check =  any(item in lista for item in listb)
        if(check):
            tot+=1
        else:
            # check =  all(item in listb for item in lista)
            check =  any(item in listb for item in lista)
            if(check):
                tot+=1
print(tot)

