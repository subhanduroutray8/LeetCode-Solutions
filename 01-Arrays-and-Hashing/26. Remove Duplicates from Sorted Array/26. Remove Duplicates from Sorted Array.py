1class Solution(object):
2    def removeDuplicates(self, nums):
3        
4        i = 0
5        if len(nums) == 1:
6            return 1
7
8        for j in range(1,len(nums)):
9            if nums[i] != nums[j]:
10                i += 1
11                nums[i] = nums[j]
12        
13        return i+1