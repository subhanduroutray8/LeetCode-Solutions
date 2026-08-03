1class Solution(object):
2    def removeElement(self, nums, val):
3        
4        :type nums: List[int]
5        :type val: int
6        :rtype: int
7        
8        while val in nums:
9            nums.remove(val)
10        return len(nums)
11        