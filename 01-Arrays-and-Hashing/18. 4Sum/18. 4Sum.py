1class Solution(object):
2    def fourSum(self, nums, target):
3        
4        n = len(nums)
5        lst = []
6        nums = sorted(nums)
7
8        for i in range(n):
9            if i > 0 and nums[i] == nums[i-1]:
10                continue
11            for j in range(i+1,n):
12
13                if j > i + 1 and nums[j] == nums[j - 1]:
14                    continue
15
16                k = j+1
17                l = n-1
18
19                while k < l:
20                    
21                    total = nums[i] + nums[j] + nums[k] + nums[l]
22
23                    if total == target:
24                        lst.append([nums[i], nums[j], nums[k], nums[l]])
25                        
26                        while k < l and nums[k] == nums[k+1]:
27                            k += 1
28                        while k < l and nums[l] == nums[l-1]:
29                            l -= 1
30                        
31                        k += 1
32                        l -= 1
33                    
34                    elif total < target :
35                        k += 1
36                    else:
37                        l -= 1
38    
39        return lst