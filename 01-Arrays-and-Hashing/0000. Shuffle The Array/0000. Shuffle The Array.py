1class Solution(object):
2    def shuffle(self, nums, n):
3        
4        arr = []
5        l = 0
6        r = len(nums) //2
7
8        for i in range (0,len(nums)//2):
9            arr.append(nums[l])
10            arr.append(nums[r])
11            l += 1
12            r += 1
13        
14        return arr