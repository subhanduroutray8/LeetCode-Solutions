1class Solution(object):
2    def smallerNumbersThanCurrent(self, nums):
3
4        dct = {}
5        result = []
6
7        sorted_nums = sorted(nums)
8
9        for i in range(len(sorted_nums)):
10            if sorted_nums[i] not in dct:
11                dct[sorted_nums[i]] = i
12
13        for num in nums:
14            result.append(dct[num])
15
16        return result