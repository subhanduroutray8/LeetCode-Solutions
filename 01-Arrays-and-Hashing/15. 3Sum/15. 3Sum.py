1class Solution(object):
2    def threeSum(self, nums):
3        
4        n = len(nums)
5        nums = sorted(nums)
6        lst = []
7
8        for i in range(n):
9            j = i+1
10            k = n-1
11
12            if i > 0 and nums[i] == nums[i-1]:
13                continue
14
15            while j < k:
16
17                sum = nums[i]+nums[j]+nums[k]
18
19                if  sum == 0:
20                    lst.append([nums[i],nums[j],nums[k]])
21                    while j < k and nums[j] == nums[j + 1]:
22                        j += 1
23                    while j < k and nums[k] == nums[k - 1]:
24                        k -= 1
25                    j += 1
26                    k -= 1
27                elif  sum < 0:
28                    j += 1
29                elif sum > 0:
30                    k -= 1 
31        return lst