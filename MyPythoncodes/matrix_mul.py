    # Get dimensions of A and B
    # Check if multiplication is possible (cols_A must equal rows_B)
    # Initialize the result matrix C with zeros (size: rows_A x cols_B)
    # Perform matrix multiplication
    # Example matrices
    # Multiply matrices A and B
    # Print the resulting matrix    
import sys
def multiplcation(A,B):
    rA=len(A)
    rB=len(B)
    cA=len(A[0])
    cB=len(B[0])
    Z=[[0 for _ in range(cB)]for _ in range(rA)]
    if(cA != rB):
        print("matrix multiplication is not possible")
        sys.exit(0)
    else:
        for i in range(rA):
            for j in range(cB):
                for k in range(rB):
                    Z[i][j]+=A[i][k]*B[k][j]
        return Z


A= [ [1,2,3],
    [1,3,2],
    [4,5,6]]
B=  [[2,3],
     [8,9],
     [1,9] ]

result=multiplcation(A,B)
for row in result:
    print(row)