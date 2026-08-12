1class Solution(object):
2    def transpose(self, matrix):
3        r = len(matrix)
4        c = len(matrix[0])
5
6        lst = [[0] * r for _ in range(c)]
7
8        for i in range(r):
9            for j in range(c):
10                lst[j][i] = matrix[i][j]
11
12        return lst