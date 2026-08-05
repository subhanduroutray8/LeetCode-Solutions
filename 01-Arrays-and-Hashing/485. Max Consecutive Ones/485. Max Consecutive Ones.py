1class Solution(object):
2    def findMaxConsecutiveOnes(self, nums):
3
4        count = 0
5        max_count = 0
6        for i in range(0,len(nums)):
7            if nums[i] == 1:
8                count += 1
9            else:
10                count = 0
11
12            if count > max_count:
13                max_count = count
14
15        return max_count 
16
17