1class Solution(object):
2    def setZeroes(self, matrix):
3        
4        r = len(matrix)
5        c = len(matrix[0])
6
7        col = [0 for _ in range(c)]
8        row = [0 for _ in range(r)]
9
10        for i in range(r):
11            for j in range(c):
12                if matrix[i][j] == 0:
13                    row[i] = -1
14                    col[j] = -1
15
16        for i in range(r):
17            for j in range(c):
18                if row[i] == -1 or col[j] == -1:
19                    matrix[i][j] = 0
20
21        return matrix     