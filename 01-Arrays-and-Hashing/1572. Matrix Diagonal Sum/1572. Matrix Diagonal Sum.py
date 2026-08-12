1class Solution(object):
2    def diagonalSum(self, mat):
3        n = len(mat)
4        sum = 0
5
6        for i in range(n):
7            sum += mat[i][i]
8            sum += mat[i][n - 1 - i]
9
10        if n % 2 == 1:
11            sum -= mat[n // 2][n // 2]
12
13        return sum