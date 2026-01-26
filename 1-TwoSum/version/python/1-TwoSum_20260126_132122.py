# Last updated: 1/26/2026, 1:21:22 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        merged = []
4        intervals.sort()
5
6        for i in range(len(intervals)):
7            if merged and merged[-1][1] >= intervals[i][0]:
8                if merged[-1][1] < intervals[i][1]:
9                    merged[-1][1] = intervals[i][1]
10            else:
11                merged.append(intervals[i])
12        return merged