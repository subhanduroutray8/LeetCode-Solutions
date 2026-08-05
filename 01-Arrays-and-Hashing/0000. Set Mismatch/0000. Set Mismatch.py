1class Solution(object):
2    def findErrorNums(self, nums):
3        
4        missing = 0
5        duplicate = 0
6        
7        frq = {}
8
9        for i in nums:
10            if i in frq:
11                frq[i] += 1
12            else:
13                frq[i] = 1
14        
15        for i in range(1,len(nums)+1):
16            if frq.get(i, 0) == 0:
17                missing = i
18        
19        for i,j in frq.items():
20            if j == 2:
21                duplicate = i
22        
23        return [duplicate, missing]