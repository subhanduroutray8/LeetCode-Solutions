1class Solution(object):
2    def searchInsert(self, nums, target):
3        for i in nums:
4            if i >= target:
5                return nums.index(i)
6            if nums[len(nums)-1] < target:
7                return len(nums)
8        