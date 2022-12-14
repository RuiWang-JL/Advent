from functools import cmp_to_key
# with open('test.txt', 'r+') as file:
with open('13.txt', 'r+') as file:
    lines = [line.strip() for line in file.readlines()]

nl = [eval(l) for i,l in enumerate(lines) if i%3 != 2 ]
tot =0
def cmp(left,right):
    # if they are two ints, left <= right == True
    if isinstance(left,int) and isinstance(right, int):
        # good
        if left< right:
            return 1
        if left == right:
            return 0
        # not
        if left > right:
            return -1
    # at least one is list, so both to list
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    # if left list is longer, quit 
    for i in range(len(left) ):
        if len(right) <= i:
            return -1
        d = cmp(left[i], right[i])
        if d != 0:
            return d
    return len(left)<len(right)

for k in range(len(nl)):
    if k % 2 ==1: 
        yes = cmp(nl[k-1], nl[k])
        if yes == 1:
            tot+=(k//2+1)

nl.append([[2]])
nl.append([[6]])
nl.sort(key = cmp_to_key(lambda x, y:-cmp(x, y)))
print((nl.index([[2]])+1) *(nl.index([[6]])+1) ) 
print(tot)