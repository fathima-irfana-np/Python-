#number reverse
n=input("enter number :")
n=n.rstrip('0')
L=[]
length=len(n)
while (length >0):
        L. append(n[length -1])
        length-=1
print("". join(L))



#
n=input("enter number :")
n=n.rstrip('0')
n=n[::-1]
print(n)