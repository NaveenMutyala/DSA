def pascalTriangle(n : int) -> List[List[int]]:
    # Write your code here.
    result = []
    for i in range(1,n+1):
        result.append(generate_row(i))
    return result
def generate_row(row):
    ans =1
    ansRow=[1]
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ansRow.append(ans)

    return ansRow
# or

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = []

        for i in range(A):
            pascals_triangle.append([1]*(i+1))

        for i in range(2,A):
            for j in range(1,i):
                pascals_triangle[i][j] = pascals_triangle[i-1][j-1] + pascals_triangle[i-1][j]

        return pascals_triangle

# input 5
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
