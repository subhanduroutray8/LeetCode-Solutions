1class Solution(object):
2    def myPow(self, x, n):
3        if n == 0:
4            return 1
5        if n < 0:
6            x = 1 / x
7            n = -n
8        half = self.myPow(x, n // 2)
9        if n % 2 == 0:
10            return half * half
11        else:
12            return half * half * x