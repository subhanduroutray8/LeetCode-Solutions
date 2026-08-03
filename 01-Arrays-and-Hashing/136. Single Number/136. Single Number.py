1class Solution(object):
2    def singleNumber(self, nums):
3        dct = {}
4        for i in nums:
5            if i in dct:
6                dct[i] += 1
7            else:
8                dct[i] = 1
9        for key, val in dct.items():
10            if val == 1:
11                return key
12
13        