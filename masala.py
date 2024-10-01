import os
os.system("cls")

ls = [("k", 7000),("p", 5000),("y", 19000),("s", 12000),("n", 8000)]

sortla = sorted(ls, key= lambda i : i[1])
sortla2 = sorted(ls, key=lambda i : i)
sortla3 = sorted(ls, key=lambda i : i[0][0])
print(sortla)
print(sortla2)
print(sortla3)