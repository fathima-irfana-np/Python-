n=int(input("ff"))
list1=[int(input()) for i in range(n)]

set1=set(list1)
dict1={}
new=[]
length=len(list1)

while(length!=0):
    list1.pop(0)
    set1=set(list1)
    for element in set1:
        count=list1.count(element)
        dict1[element]=count
    maxV=max(dict1.values())
    for x in dict1.keys():
        if dict1[x]==maxV:
            getKey=x
            break
    new.append(getKey)
    length-=1


new.append(-1)

print(new)