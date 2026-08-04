1class Solution(object):
2    def findMissingElements(self, nums):
3        
4        :type nums: List[int]
5        :rtype: List[int]
6        
7        new = []
8
9        mini = min(nums)
10        maxi = max(nums)
11
12        for i in range(mini + 1, maxi):
13            if i not in nums:
14                new.append(i)
15                    
16        return new