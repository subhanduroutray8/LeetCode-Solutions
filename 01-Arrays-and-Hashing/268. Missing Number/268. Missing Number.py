1class Solution(object):
2    def missingNumber(self, nums):
3        
4        st = set(nums[:])
5        for i in range(0,len(nums)+1):
6            if i not in st:
7                return i