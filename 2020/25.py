import re
from  itertools import product
from collections import defaultdict,deque,Counter
import time
import math
start_time = time.time()

cp = 1717001
dp = 523731
#cl = math.log(cp,7)
#dl = math.log(dp,7)

y = 1
cl=0
while y != cp:
    y = 7*y%20201227
    cl +=1
#print(cl)

y = 1
dl=0
while y != dp:
    y = 7*y%20201227
    dl +=1
#print(dl)

x = 1
print(cl,dl)
for i in range(0,int(cl)):
    x = dp * x % 20201227
print(x)


print("--- %s seconds ---" % (time.time() - start_time))
