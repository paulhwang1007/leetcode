# Last updated: 7/26/2026, 3:53:32 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            
            left, right = 0, len(matrix[i]) - 1
            while left <= right:
                mid = (left + right) // 2

                if matrix[i][mid] < target:
                    left = mid + 1
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    return True
        return False