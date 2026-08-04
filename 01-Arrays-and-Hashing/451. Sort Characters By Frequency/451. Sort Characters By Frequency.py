1class Solution(object):
2    def frequencySort(self, s):
3
4        dct = {}
5        st = 
6
7        for ch in s:
8            if ch in dct:
9                dct[ch] += 1
10            else:
11                dct[ch] = 1
12
13        sorted_items = sorted(dct.items(), key=lambda x: x[1], reverse=True)
14
15        for ch, freq in sorted_items:
16            st += ch * freq
17
18        return st