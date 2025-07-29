#index of fibonacci number without recursion
def fibo(num):
    LIST=[]
    if num<=1:
        return 1
    else:
        c,b,i,a=0,1,1,0
        while(i<=num):
            LIST.append(c)
            c=a+b
            a=b
            b=c
            i+=1
        return(LIST[num-1])

n=int(input("enter index"))
print(fibo(n))

def fibo(num):
    if num<=1:
        return 1
    else:
        c,b,i,a=0,1,1,0
        while(i<=num):
            if(i==num):
                return c
            c=a+b
            a=b
            b=c
            i+=1

n=int(input("enter index"))
print(fibo(n))