1class Solution(object):
2    def intersection(self, nums1, nums2):
3        
4        st = set(nums2[:])   
5        lst = []
6
7        for i in nums1:
8            if i in st:
9                lst.append(i)
10
11        return list(set(lst))     