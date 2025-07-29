#lets add prefx
z=int(input("enter the size"))
N=input("enter the number")
if len(N)==z:
    print(N)
else:
    remain=z-len(N)
    remain=remain*'0'+N
    print(remain)