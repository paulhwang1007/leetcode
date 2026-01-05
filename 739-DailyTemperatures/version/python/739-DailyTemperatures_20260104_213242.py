# Last updated: 1/4/2026, 9:32:42 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        answer = [0] * len(temperatures)
4        decr_temps = []
5
6        for i, t in enumerate(temperatures):
7            while decr_temps and t > decr_temps[-1][1]:
8                index, temp = decr_temps.pop()
9                answer[index] = i - index
10            decr_temps.append([i, t])
11        
12        return answer
13