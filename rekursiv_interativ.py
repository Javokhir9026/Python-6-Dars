import os
os.system("cls")

def Interativ_sana(son:int):
    for i in range(1,son + 1):
        print(i)

def Rekursiv_sana(son:int):
    if son > 0:
        Rekursiv_sana(son-1)
        print(son)

def Interativ_Faktorial(son:int):
    f = 1
    for i in range(1,son + 1):
        f = f * i
    print("Faktorial ==> ", f)

def Rekursiv_Faktorial(son:int):
    if son == 1:
        return(son)
    else:
        return son * Rekursiv_Faktorial(son-1)

son = int(input("SON: "))
Interativ_sana(son)
Rekursiv_sana(son)
Interativ_Faktorial(son)
fk = Rekursiv_Faktorial(son)
print("Faktorial ==> ",fk)