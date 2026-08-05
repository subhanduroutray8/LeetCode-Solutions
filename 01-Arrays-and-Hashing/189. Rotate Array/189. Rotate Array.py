1class Solution(object):
2    def rotate(self, nums, k):
3        
4        k %= len(nums)
5        
6        def reverse(nums, start, end):
7
8            while start < end:
9                nums[start], nums[end-1] = nums[end-1], nums[start]
10                start += 1
11                end -= 1
12        
13        reverse(nums, len(nums)-k, len(nums))
14        reverse(nums, 0, len(nums)-k)
15        reverse(nums, 0, len(nums))
16
17        return nums