# Last updated: 1/5/2026, 10:35:58 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res = [0] * len(temperatures)
4        stack = []
5
6        for i, t in enumerate(temperatures):
7            while stack and t > stack[-1][1]:
8                index, temp = stack.pop()
9                res[index] = i - index
10            stack.append([i, t])
11        
12        return res