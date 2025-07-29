r = int(input("Enter the number of rows: "))  
c = int(input("Enter the number of cols: "))  
for i in range(r, 0, -1):  
    stars = '*' * (2 * i - 1)
    print(stars.center(2 * r - 1)) 
for i in range(2, r+1, 1):  
    stars = '*' * (2 * i - 1)
    print(stars.center(2 * r - 1)) 
    #r's value is constent
for i in range (r,0,-1):
    stars='*'*(2*i-1)
    print(stars.center(2*r-1))
