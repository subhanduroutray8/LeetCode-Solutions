1class Solution(object):
2    def smallerNumbersThanCurrent(self, nums):
3        
4        lst = []
5        num = nums[:]
6        num.sort()
7        freq = {}
8
9        for i in num :
10            if i not in freq:
11                freq[i] = num.index(i)
12
13        for i in nums:
14            lst.append(freq[i])
15
16        return lst