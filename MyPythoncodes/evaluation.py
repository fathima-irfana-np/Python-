module=int(input("modules?"))
l=[]
sum=0
mark=[int(input(""))for i in range(module*2)]
print(mark)
for i in range(0,len(mark),2):
    if(mark[i]>mark[i+1]):
        sum+=mark[i]
    else:
        sum+=mark[i+1]
print(sum)