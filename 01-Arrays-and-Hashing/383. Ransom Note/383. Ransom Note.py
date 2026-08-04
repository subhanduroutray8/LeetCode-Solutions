1class Solution(object):
2    def canConstruct(self, ransomNote, magazine):
3        
4        dct = {}
5        for i in magazine:
6            if i in dct:
7                dct[i] += 1
8            else:
9                dct[i] = 1
10        for i in ransomNote:
11            if i in dct and dct[i]>0:
12                dct[i] -= 1
13            else:
14                return False
15        return True