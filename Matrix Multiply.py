# def matrix(m,n):
#     col = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             inp = int(input(f"Enter the [{i}][{j}] element:"))
#             row.append(inp)
#         col.append(row)
#     return col

# # # Multiplying matrices
# def multiply(A):
#     col = []
#     for i in range(len(A)+1):
#         row = []
#         for j in range(len(B[0])):
#             print(f"value of i={i} and j={j}")
#             multiple = A[i][j]*B[i][j]+A[i][j+1]*B[i+1][j]
#             print(f"row: {multiple}")
#             row.append(multiple)
#             print("appended row ", row)
#         col.append(row)
#         print("appended column",col)
#     return col

# print("Enter the Matrix A: ")
# m = int(input("Enter the number of row:"))
# n = int(input("Enter the number of column:"))
# A = matrix(m, n)

# print("Enter the matrix B: ")
# m = int(input("Enter the number of row:"))
# n = int(input("Enter the number of column:"))
# B = matrix(m, n)

# multi = multiply(A)

# print("A =", A)
# print("B =", B)
# print("AxB =", multi)



X = [[1,0,3],
     [3,3,0],
     [0,3,3]]
Y = [[1,0,3],
     [3,0,0],
     [0,0,3]]
C = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(C)): # length of row of first matrix
    for j in range(len(C[0])): # length of column of second matrix
        for k in range(len(Y)): # length of column of first matric i.e. (common order)
            C[i][j] += X[i][k] * Y[k][j]

for row in C:
    print(row)

