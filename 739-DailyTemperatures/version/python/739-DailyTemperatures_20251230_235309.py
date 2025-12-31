# Last updated: 12/30/2025, 11:53:09 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        output = [0] * len(temperatures)
4        stack = [] # store [temperature, index]
5
6        for i, t in enumerate(temperatures):
7            while stack and t > stack[-1][0]:
8                stackT, stackI = stack.pop()
9                output[stackI] = i - stackI
10            stack.append([t, i])
11        return output