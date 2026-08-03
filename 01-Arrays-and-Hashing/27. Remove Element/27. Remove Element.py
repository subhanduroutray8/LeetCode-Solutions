1class Solution(object):
2    def removeElement(self, nums, val):
3        while val in nums:
4            nums.remove(val)
5        return len(nums)
6        