1class Solution(object):
2    def findMissingElements(self, nums):
3
4        
5        lst = []
6        s = min(nums)
7        l = max(nums)
8
9        st = set(nums)
10
11        for i in range(s,l):
12            if i not in st:
13                lst.append(i)
14        
15        return lst