

def zeroMatrix(matrix, n, m):
    # Write your code here.
    row =[-1]*n
    col =[-1]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=0
                col[j]=0
    for i in range(n):
        for j in range(m):
            if row[i]==0 or col[j]==0:
                matrix[i][j]=0
    return matrix

## if a row or col contains a zero making entire row and column to zero

#input
# 2 3
# 2 4 3
# 1 0 0
# output
# 2 0 0 
# 0 0 0 
