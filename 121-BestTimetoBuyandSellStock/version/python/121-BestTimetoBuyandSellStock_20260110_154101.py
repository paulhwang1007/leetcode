# Last updated: 1/10/2026, 3:41:01 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        profit = 0
4
5        for i in range(len(prices)):
6            if i == len(prices) - 1 or prices[i] >= prices[i+1]:
7                continue
8            
9            j = i + 1
10            while j < len(prices) and prices[i] < prices[j]:
11                profit = max(profit, prices[j] - prices[i])
12                j += 1
13            
14        return profit
15