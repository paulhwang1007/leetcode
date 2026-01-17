# Last updated: 1/17/2026, 12:39:07 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        for i in range(len(matrix)):
4            if matrix[i][-1] < target:
5                continue
6            
7            left, right = 0, len(matrix[i]) - 1
8            while left <= right:
9                mid = (left + right) // 2
10
11                if matrix[i][mid] < target:
12                    left = mid + 1
13                elif matrix[i][mid] > target:
14                    right = mid - 1
15                else:
16                    return True
17        return False