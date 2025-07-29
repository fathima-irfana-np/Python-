#print nth fibonacci number with recursion
def fibo(num):
    if num<=1:
        return 1
    else:
        return fibo(num-2)+fibo(num-1)

n=int(input("enter index"))
result=fibo(n-1)
print(result)