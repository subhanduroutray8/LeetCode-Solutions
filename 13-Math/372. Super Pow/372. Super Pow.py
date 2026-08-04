1class Solution(object):
2    def superPow(self, a, b):
3        c=0
4        for i in b:
5            c = (c*10) + i
6        return pow(a,c,1337)