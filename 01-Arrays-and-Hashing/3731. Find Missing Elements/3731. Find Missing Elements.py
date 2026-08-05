1class Solution(object):
2    def findMissingElements(self, nums):
3        
4        :type nums: List[int]
5        :rtype: List[int]
6        
7        lst = []
8        s = min(nums)
9        l = max(nums)
10
11        st = set(nums)
12
13        for i in range(s,l):
14            if i not in st:
15                lst.append(i)
16        
17        return lst