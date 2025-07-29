#sort array use bubble sort
def sort_array(List):
    for i in range(len(List)+1): # i=0,i<len(List)+1,i++ okay
        for j in range(i,len(List)): # j=i,j<len(List),j++ okay
            if(List[i]>List[j]):
                temp=List[i]
                List[i]=List[j]
                List[j]=temp
    return List

size=int(input("enter the size of array"))
print("enter elements")
L=[int(input("")) for i in range(size)]
result=sort_array(L)
print(result)