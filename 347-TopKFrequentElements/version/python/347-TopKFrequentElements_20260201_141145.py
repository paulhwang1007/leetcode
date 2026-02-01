# Last updated: 2/1/2026, 2:11:45 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        res = []
4        intervals.sort()
5
6        for i in range(len(intervals)):
7            if res and res[-1][1] >= intervals[i][0]:
8                if res[-1][1] < intervals[i][1]:
9                    res[-1][1] = intervals[i][1]
10            else:
11                res.append(intervals[i])
12        return res