# Adding two matrices of mxn order matrix

# m = int(input("Enter the no. of rows of matrix: "))
# n = int(input("Enter the no. of columns of matrix: "))
# print(f"The order of matrix is {m}x{n}")

# Taking the matirx element inputs from the user 
def matrix(m,n):
    col = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter col[{i}][{j}] elment: "))
            row.append(inp)
        col.append(row)
    return col

# Adding up the matrices
def add(A):
    col = []
    added = []
    for i in range(len(A)):
        row = []
        for j in range(len(A)):
            added =  A[i][j]+B[i][j]
            row.append(added)
        col.append(row)
    return col


# Taking the order of matrix
m = int(input("Enter the number of row: "))
n = int(input("Enter the number of column: "))

# Displaying the matrix
print("Enter the Matrix A:")
A = matrix(m,n)
print("Enter the matrix B:")
B = matrix(m,n)

print("A =", A)
print("B =", B)
sum = add(A) 
print(f"A+B =", sum)