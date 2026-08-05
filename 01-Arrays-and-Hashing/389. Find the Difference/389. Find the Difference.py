1class Solution(object):
2    def findTheDifference(self, s, t):
3        
4        dct = {}
5        for i in s:
6            if i in dct:
7                dct[i] += 1
8            else:
9                dct[i] = 1
10        
11        for i in t:
12            if i in dct and dct[i] > 0:
13                dct[i] -= 1
14            else:
15                return i