def add(a:int, b:int):
    x = lambda a,b:a+b
    print(x(a,b))

import os
os.system("cls")

ls = [1,9,6,4,5,7,2]
kattasi = 0
for i in ls:
    if kattasi < i:
        kattasi = i
l = 0
ylist = list()
s = 1
for j in ls:
    for i in range(len(ls)):
        if j  == kattasi-i:
            ylist.append(j)

print(ylist)
