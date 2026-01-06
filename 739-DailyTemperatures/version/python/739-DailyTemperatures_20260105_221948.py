# Last updated: 1/5/2026, 10:19:48 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        cars = [[p, s] for p,s in zip(position, speed)]
4        times = []
5
6        for p,s in sorted(cars)[::-1]:
7            times.append((target - p) / s)
8
9            if len(times) >= 2 and times[-1] <= times[-2]:
10                times.pop()
11            
12        return len(times)