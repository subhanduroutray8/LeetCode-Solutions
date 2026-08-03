1class Solution(object):
2    def removeDuplicates(self, nums):
3        for x in nums[:]:
4            while nums.count(x) > 1:
5                nums.remove(x)
6        return len(nums)
7               