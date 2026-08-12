# Last updated: 8/11/2026, 11:04:17 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stack = []
4        days = [0] * len(temperatures)
5
6        for i in range(len(temperatures)):
7            while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]: 
8                top_idx = stack.pop()
9                days[top_idx] = i - top_idx
10
11            stack.append(i)
12            
13        return days
14        