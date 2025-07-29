#matrix multiplication
def multiplication(A,B,colA,colB,rowA,rowB):
    Z=[ [0 for _ in range(colB)] for _ in range(rowA)]
    if(colA!=rowB):
        print("multiplication is not possible")
        return []

    for i in range(rowA):
        for j in range(colB):
            for k in range(rowB):
                Z[i][j]+=A[i][k]*B[k][j]
    return Z

rowA=int(input("enter the size of row"))
colA=int(input("enter the size of cols"))
A=[[int(input("")) for i in range(colA)]for j in range(rowA)]
for row in A:
    print(row)
rowB=int(input("enter the size of row1"))
colB=int(input("enter the size of cols2"))
B=[[int(input("")) for i in range(colB)]for j in range(rowB)]
for row in B:
    print(row)
result=multiplication(A,B,colA,colB,rowA,rowB)
for row in result:
    print(row)