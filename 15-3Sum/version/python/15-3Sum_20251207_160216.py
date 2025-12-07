# Last updated: 12/7/2025, 4:02:16 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        arr = []
4        intervals.sort()
5
6        for i in range(len(intervals)):
7            if arr and arr[-1][1] >= intervals[i][0]:
8                if arr[-1][1] < intervals[i][1]:
9                    arr[-1][1] = intervals[i][1]
10            else:
11                arr.append(intervals[i])
12        return arr