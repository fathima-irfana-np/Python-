
for j in range(0,10):
    for i in range(0,10):
        if(i==0 or i==9 or i==j or i+j==9):
            print("*", end='')
            print("\t", end='')
        else:
            print("\t", end='')
            
    print("\n")
