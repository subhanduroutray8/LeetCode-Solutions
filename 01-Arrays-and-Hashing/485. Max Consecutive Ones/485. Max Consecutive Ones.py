1class Solution(object):
2    def findMaxConsecutiveOnes(self, nums):
3        
4        max = 0
5        count = 0
6        for i in nums:
7            if i == 1:
8                count += 1
9            else:
10                count = 0
11            if count > max:
12                max = count 
13
14        return max