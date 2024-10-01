import os
os.system("cls")

def Chiqar(st:str, ind = int):
    if len(st) == ind:
        return 0
    print(st[ind])
    Chiqar(st,ind+1)

s = input("Matn : ")
Chiqar(s,0)