def recur(digit):
    if digit<=0:
        return 0
    return (digit%10)+recur(digit//10)
num=int(input("num:"))
result=recur(num)
print("the result is ",result )


 