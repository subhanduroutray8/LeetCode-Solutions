1class Solution(object):
2    def isAnagram(self, s, t):
3        
4        dct_s = {}
5        dct_t = {}
6
7        for i in s:
8            if i in dct_s:
9                dct_s[i] += 1
10            else:
11                dct_s[i] = 1
12        
13        for i in t:
14            if i in dct_t:
15                dct_t[i] += 1
16            else:
17                dct_t[i] = 1    
18
19        if dct_s == dct_t:
20            return True
21        else:
22            return False