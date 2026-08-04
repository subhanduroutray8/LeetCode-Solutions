1class Solution(object):
2    def firstUniqueEven(self, nums):
3        
4        for i in nums:
5            if nums.count(i) == 1 and i%2 == 0:
6                return i
7        return -1   