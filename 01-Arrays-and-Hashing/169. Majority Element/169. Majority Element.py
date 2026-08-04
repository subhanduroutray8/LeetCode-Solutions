1class Solution(object):
2    def majorityElement(self, nums):
3        
4        maj = len(nums)//2
5        dct = {}
6        for i in nums:
7            if i in dct:
8                dct[i] += 1
9            else:
10                dct[i] = 1
11        for i,j in dct.items():
12            if j > maj:
13                return i