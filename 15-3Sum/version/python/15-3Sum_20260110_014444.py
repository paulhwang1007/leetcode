# Last updated: 1/10/2026, 1:44:44 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        i, j = 0, len(height) - 1
4        max_area = 0
5
6        while i < j:
7            area = min(height[i], height[j]) * (j - i)
8            max_area = max(max_area, area)
9
10            if height[i] <= height[j]:
11                i += 1
12            else:
13                j -= 1
14        
15        return max_area
16            