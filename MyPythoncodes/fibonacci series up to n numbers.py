#fibonacci series up to n numbers

n=int(input("enter a number"))
a=0
b=1
c=0
print(a)
while(c<=n):
    print(c)
    c=a+b
    a=b
    b=c
    
# fibonacci series up to n numbers

n=int(input("enter a number"))
a=0
b=1
c,i=0,1
print(a)
print(b)
while(i!=n-1):
    c=a+b
    a=b
    b=c
    print(c)
    i+=1
    

n=int(input("enter a number"))
a=0
b=1
c,i=0,1
while(i!=n-1):
    c=a+b
    a=b
    b=c
    i+=1
    if(i==n-1):
        print(c)