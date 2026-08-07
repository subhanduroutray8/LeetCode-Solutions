1class Solution(object):
2    def moveZeroes(self, nums):
3        
4        n = len(nums)
5        if n == 1:
6            return nums
7        
8        i = 0
9        for j in range(0,n):
10            if nums[j] != 0:
11                    nums[i], nums[j] = nums[j], nums[i]
12                    i += 1
13        
14        return nums