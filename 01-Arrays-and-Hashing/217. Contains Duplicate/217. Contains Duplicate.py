1class Solution(object):
2    def containsDuplicate(self, nums):
3        if len(nums) == len(set(nums)):
4            return False
5        else:
6            return True