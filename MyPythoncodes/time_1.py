r=int(input("enter the number of rows"))
r=r//2
for i in range(0,r,1):
         stars='*'*(2*i-1)
         print(stars.center(2*r-1))
for i in range(r,0,-1):
         stars='*'*(2*i-1)
         print(stars.center(2*r-1))


