# Last updated: 12/8/2025, 2:19:32 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        for i in range(len(matrix)):
4            if matrix[i][-1] < target:
5                continue
6            left, right = 0, len(matrix[i]) - 1
7            while left <= right:
8                mid = (left + right) // 2
9                if matrix[i][mid] > target:
10                    right = mid - 1
11                elif matrix[i][mid] < target:
12                    left = mid + 1
13                else:
14                    return True
15        return False
16            
17            