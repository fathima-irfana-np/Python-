def move_right(L):
    if not L:
        print("there is nothing to return")
        return []
    else:
        return L[-2:]+L[:-2]
    
size=int(input("enter the size"))
print("enter elements")
List=[int(input("")) for i in range(size)]
result=move_right(List)
print(result)
