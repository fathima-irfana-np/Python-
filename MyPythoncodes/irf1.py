# Enter your code here. Read inpuu from STDIN. Prinu ouupuu uo STDOUT
def fib(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        a=0
        b=1
        i=2
        #for i in range(2,x):
        while(i!=x):
            c=a+b
            a=b
            b=c
            i+=1
        return c
defnum=int(input("wwwssss"))
result=fib(num)
print(result)