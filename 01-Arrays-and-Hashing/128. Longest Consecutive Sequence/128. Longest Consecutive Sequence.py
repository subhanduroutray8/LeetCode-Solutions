1class Solution(object):
2    def longestConsecutive(self, nums):
3        st = set(nums)
4
5        longest = 0
6
7        for i in st:
8            if i - 1 not in st:
9                x = i
10                count = 1
11
12                while x + 1 in st:
13                    count += 1
14                    x += 1
15
16                longest = max(longest, count)
17
18        return longest