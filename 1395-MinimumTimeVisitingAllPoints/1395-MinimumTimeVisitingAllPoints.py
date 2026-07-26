# Last updated: 7/26/2026, 3:52:58 PM
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        x1, y1 = points[0]

        for i in range(1, len(points)):
            x2, y2 = points[i]
            time += max(abs(x2 - x1), abs(y2 - y1))
            x1, y1 = x2, y2

        return time