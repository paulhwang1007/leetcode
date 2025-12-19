# Last updated: 12/18/2025, 10:57:56 PM
1class Solution:
2    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
3        time = 0
4        x1, y1 = points.pop()
5
6        while points:
7            x2, y2 = points.pop()
8            time += max(abs(y2 - y1), abs(x2 - x1))
9            x1, y1 = x2, y2
10        return time