1class Solution(object):
2    def findMedianSortedArrays(self, nums1, nums2):
3        
4        nums = nums1 + nums2
5        nums.sort()
6
7        n = len(nums)
8
9        if n % 2 == 0:
10            return (nums[n//2] + nums[(n//2)-1])/2.0
11        
12        return nums[n//2]
13        