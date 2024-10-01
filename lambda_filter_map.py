import os
os.system("cls")

def son(s:int):
    yig = s + 10
    return yig

print(son(3))

x = lambda i : i + 10
print(x(5))

kub = lambda x : x * x * x
print(kub(5))

ls = [1,10,2,30,3,30,4,40,5,50]
print("sortlanmagan list: \n", ls)
print()
sort_son = sorted(ls, key= lambda i : i)
print("Sortlangan list: \n", sort_son)

                #! F I L T E R
                #! M A P
reqam = [1,2,3,4,5]
juft = list(map(lambda i: i % 2 == 0, ls))
print(juft)

palindrom = ["aziz","kiyik","non","123","121"]
p = list(filter(lambda p : (p == p[::-1]), palindrom))
print(p)