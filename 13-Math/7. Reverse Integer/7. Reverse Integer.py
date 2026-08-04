1class Solution(object):
2    def reverse(self, x):
3        
4        n = abs(x)
5        rev = 0
6        if n == 0 :
7            return 0
8        while n > 0:
9            rev = (rev*10) + n%10
10            n = n//10
11        
12        if rev <= 2147483647 and rev >=  -2147483648:
13            if x < 0:
14                return rev*-1
15            else:
16                return rev
17        else:
18            return 0