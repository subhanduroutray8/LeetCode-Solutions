1class Solution(object):
2    def removeDuplicates(self, nums):
3        
4        i, j = 0, 1
5        n = len(nums)
6
7        while j < n:
8            if nums[j] != nums[i]:
9                nums[i+1], nums[j] = nums[j], nums[i+1]
10                i += 1
11            j += 1
12
13        return i+1