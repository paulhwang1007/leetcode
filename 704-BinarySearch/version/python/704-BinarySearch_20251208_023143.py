# Last updated: 12/8/2025, 2:31:43 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        ROWS, COLS = len(matrix), len(matrix[0])
4        top, bot = 0, ROWS - 1
5
6        while top <= bot:
7            row = (top + bot) // 2
8            if target > matrix[row][-1]:
9                top = row + 1
10            elif target < matrix[row][0]:
11                bot = row - 1
12            else:
13                break
14        
15        if not (top <= bot):
16            return False
17        row = (top + bot) // 2
18        l, r = 0, COLS - 1
19
20        while l <= r:
21            m = (l + r) // 2
22            if target > matrix[row][m]:
23                l = m + 1
24            elif target < matrix[row][m]:
25                r = m - 1
26            else:
27                return True
28        return False