1class Solution(object):
2    def containsDuplicate(self, nums):
3        
4        dct = {}
5
6        for i in range(len(nums)):
7            if nums[i] in dct:
8                return True
9            dct[nums[i]] = 1
10        
11        return False