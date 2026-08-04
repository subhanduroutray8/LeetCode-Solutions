1class Solution(object):
2    def isPalindrome(self, x):
3
4        n = x
5        rev = 0
6
7        if x < 0:
8            return False
9        if n == 0 :
10            return True
11        while n > 0:
12            rev = (rev*10) + n%10
13            n = n//10
14
15        if rev == x:
16            return True
17        else:
18            return False