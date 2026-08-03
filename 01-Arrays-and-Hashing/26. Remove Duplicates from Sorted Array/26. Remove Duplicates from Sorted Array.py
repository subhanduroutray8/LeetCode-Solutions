1class Solution(object):
2    def removeDuplicates(self, nums):
3        
4        :type nums: List[int]
5        :rtype: int
6        
7        for i in nums:
8            while nums.count(i) > 1:
9                nums.remove(i) 
10        return len(nums)    