1class Solution(object):
2    def majorityElement(self, nums):
3        
4        lst = []
5        maj = len(nums)//3
6        dct = {}
7        for i in nums:
8            if i in dct:
9                dct[i] += 1
10            else:
11                dct[i] = 1
12        for i,j in dct.items():
13            if j > maj:
14                lst.append(i)
15        return lst