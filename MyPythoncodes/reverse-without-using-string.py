num=int(input("enter a number"))
result=0
while(num>0):
    result=result*10+(num%10)
    num=num//10
print(result)