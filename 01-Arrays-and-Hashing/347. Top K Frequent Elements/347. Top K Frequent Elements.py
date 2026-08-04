1class Solution(object):
2    def topKFrequent(self, nums, k):
3
4        dct = {}
5        for i in nums:
6            if i in dct:
7                dct[i] += 1
8            else:
9                dct[i] = 1
10
11        sorted_items = sorted(dct.items(), key=lambda x: x[1], reverse=True)
12
13        ans = []
14        for num, freq in sorted_items[:k]:
15            ans.append(num)
16
17        return ans