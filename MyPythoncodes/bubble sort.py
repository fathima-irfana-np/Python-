#sort array use bubble sort
def sort_array(List):
    i=0
    while(i<len(List)+1):
        j=i
        while(j<len(List)):
            if(List[i]>List[j]):
                temp=List[i]
                List[i]=List[j]
                List[j]=temp
            j+=1
        i+=1
    return List

size=int(input("enter the size of array"))
print("enter elements")
L=[int(input("")) for i in range(size)]
result=sort_array(L)
print(result)