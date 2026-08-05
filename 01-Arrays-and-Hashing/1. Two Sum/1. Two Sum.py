1class Solution(object):
2    def twoSum(self, nums, target):
3
4        dct = {}
5        for i in range(len(nums)):
6            complement = target - nums[i]
7
8            if complement in dct:
9                return [dct[complement], i]
10            dct[nums[i]] = i