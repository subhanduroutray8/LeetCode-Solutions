1class Solution(object):
2    def concatWithReverse(self, nums):
3        
4        ans1 = nums
5        ans =  ans1 + nums[::-1]
6        return ans
7