List1=[1,1,2,2,1,3,4]
List2=[]

for x in List1:
    if x not in List2:
        List2.append(x)
        
for x in List2:
    count=0
    for y in List1:
        if y==x:
            count+=1
    print(f"{x} occured {count} times")
    
        