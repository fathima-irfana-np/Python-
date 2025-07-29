#matrix multiplication
def multiplication(A,B,colA,colB,rowA,rowB):
    Z=[ [0 for _ in range(colA)] for _ in range(rowB)]
    if(colA!=rowB):
        print("multiplication is not possible")
        return 0

    for i in range(rowA):
        for j in range(colB):
            for k in range(rowB):
                Z[i][j]+=A[i][k]*B[k][j]
    return Z

rowA=int(input("enter the size of row"))
colA=int(input("enter the size of cols"))
A=[[int(input("")) for i in range(colA)]for j in range(rowA)]
rowB=int(input("enter the size of row"))
colB=int(input("enter the size of cols"))
B=[[int(input("")) for i in range(colB)]for j in range(rowB)]
result=multiplication(A,B,colA,colB,rowA,rowB)
for row in result:
    print(row)