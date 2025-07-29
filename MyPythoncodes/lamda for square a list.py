size=int(input("enter size of list"))
print("enter list elements")
L=[int(input("")) for i in range(size)]
L=list(map(lambda x:x*x ,L))
print(L)

L = [1, 2, 3, 4, 5, 6]
L = list(map(lambda x:x if x % 2 == 0 else None, L))
L=list(filter(None,L))
print(L) 
