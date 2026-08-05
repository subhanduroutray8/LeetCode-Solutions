1class Solution(object):
2    def findDisappearedNumbers(self, nums):
3        
4        st = set(nums)
5        lst = []
6
7        maxm = max(nums)
8        for i in range(1,len(nums)+1):
9            if i not in st:
10                lst.append(i)
11
12        return lst