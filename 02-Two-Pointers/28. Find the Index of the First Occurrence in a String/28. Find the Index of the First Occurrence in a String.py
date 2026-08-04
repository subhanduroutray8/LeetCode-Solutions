1class Solution(object):
2    def strStr(self, haystack, needle):
3        
4        if needle not in haystack:
5            return -1
6        else:
7            return haystack.find(needle)