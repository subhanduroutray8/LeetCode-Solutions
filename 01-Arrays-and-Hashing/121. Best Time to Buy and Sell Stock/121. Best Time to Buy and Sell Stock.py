1class Solution(object):
2    def maxProfit(self, prices):
3        min_price = float(inf)
4        max_profit = 0
5
6        for price in prices:
7            if price < min_price:
8                min_price = price
9
10            profit = price - min_price
11
12            if profit > max_profit:
13                max_profit = profit
14
15        return max_profit