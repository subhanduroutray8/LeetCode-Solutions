1class Solution(object):
2    def rotate(self, matrix):
3        
4        n = len(matrix)
5
6        for i in range(n):
7            for j in range(i+1,n):
8                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
9
10        for row in matrix:
11            row.reverse()     
12
13        return matrix   