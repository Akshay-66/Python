r = int(input("Enter Matrix 1 row: "))
c = int(input("Enter Matrix 1 column: "))
r1 = int(input("Enter Matrix 2 row: "))
c1 = int(input("Enter Matrix 2 Column: "))
matrix1 = []
matrix2 = []
if r != c1:
    print("Matrix multiplication not possible")
    exit()
for i in range(r):
    ro = list(map(int,input().strip().split()))
    matrix1.append(ro)
for i in range(r1):
    ro = list(map(int,input().strip().split()))
    matrix2.append(ro)
res = [[0 for x in range(c1)] for y in range(r)]
 
# explicit for loops
for i in range(r):
    for j in range(c1):
        for k in range(r1):
 
            # resulted matrix
            res[i][j] += matrix1[i][k] * matrix2[k][j]
 
print(res)
