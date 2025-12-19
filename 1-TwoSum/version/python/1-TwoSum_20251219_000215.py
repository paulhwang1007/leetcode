# Last updated: 12/19/2025, 12:02:15 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        left, right = 0, 1
4        profit = 0
5
6        while right < len(prices):
7            if prices[left] < prices[right]:
8                profit = max(profit, prices[right] - prices[left])
9            else:
10                left = right
11
12            right += 1
13        return profit
14