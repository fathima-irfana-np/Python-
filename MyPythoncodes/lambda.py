size=int(input("enter size of your list"))
print("enter elements for your list")
L=[]
for i in range(size):
    item=input("")
    L.append(item)
L=list(map(lambda x:"Rs"+x,L))
print(L)