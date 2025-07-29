#factorial without recursion
def fact(n):
    result=1
    if n==1 or n==0:
        return 1
    else:
        for i in range(1,n+1,1):
            result=result*i
        return result

n=int(input("enter a number"))
print(fact(n))


    