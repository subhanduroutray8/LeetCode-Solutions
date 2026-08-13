1class Solution(object):
2    def spiralOrder(self, matrix):
3
4        result = []
5
6        top, left = 0, 0
7        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
8
9        while top <= bottom and left <= right:
10            for i in range(left, right + 1):
11                result.append(matrix[top][i])
12            top += 1
13
14            for i in range(top, bottom + 1):
15                result.append(matrix[i][right])
16            right -= 1
17
18            if top <= bottom:
19                for i in range(right, left - 1, -1):
20                    result.append(matrix[bottom][i])
21                bottom -= 1
22
23            if left <= right:
24                for i in range(bottom, top - 1, -1):
25                    result.append(matrix[i][left])
26                left += 1
27
28        return result