1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        
4        for row in matrix:
5            if target in row:
6                return True
7        return False
8        