1class Solution(object):
2    def targetIndices(self, nums, target):
3
4        lst = []
5        nums.sort()
6        for i in range(len(nums)) :
7            if nums[i] == target:
8                lst.append(i)
9        
10        return lst