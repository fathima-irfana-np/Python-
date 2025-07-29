m=int(input("enter a number m"))
n=int(input("enter a number n"))
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
if(1<=n<=26) and n<m:
    newline=''.join(list1[n-1:m])
    print(newline[::-1])
else:
    print("invalid input")