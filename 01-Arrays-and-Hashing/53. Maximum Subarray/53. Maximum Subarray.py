1class Solution(object):
2    def maxSubArray(self, nums):
3        
4        n = len(nums)
5        if n == 1:
6            return nums[0]
7        
8        max = float(-inf)
9        sum = 0
10
11        for i in nums:
12            sum += i
13            if sum > max:
14                max = sum
15            if sum < 0:
16                sum = 0
17
18        return max