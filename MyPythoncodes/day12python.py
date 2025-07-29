def matrix_multiply(A, B):
    # Get dimensions of A and B
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # Check if multiplication is possible (cols_A must equal rows_B)
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B")
    
    # Initialize the result matrix C with zeros (size: rows_A x cols_B)
    C = [[0] * cols_B for _ in range(rows_A)]
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or for k in range(rows_B)
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Multiply matrices A and B
C = matrix_multiply(A, B)

# Print the resulting matrix
for row in C:
    print(row)
