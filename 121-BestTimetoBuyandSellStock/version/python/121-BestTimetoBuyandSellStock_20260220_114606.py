# Last updated: 2/20/2026, 11:46:06 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        l, r = 0, 1
4        maxP = 0
5
6        while r < len(prices):
7            if prices[l] < prices[r]:
8                profit = prices[r] - prices[l]
9                maxP = max(maxP, profit)
10            else:
11                l = r
12            r += 1
13        
14        return maxP
15