# Last updated: 12/18/2025, 11:01:10 PM
1class Solution:
2    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
3        time = 0
4        x1, y1 = points[0]
5
6        for i in range(1, len(points)):
7            x2, y2 = points[i]
8            time += max(abs(x2 - x1), abs(y2 - y1))
9            x1, y1 = x2, y2
10
11        return time