l=[]
count=i=0
size=int(input("enter the size of list"))
print("enter elements")
for i in range(size):
       elements=input("")
       l.append(elements)
for x in l:
       length=len(x)
       for i in range(0,length):
              if x[i]=='a':
                    count+=1

print(count)     