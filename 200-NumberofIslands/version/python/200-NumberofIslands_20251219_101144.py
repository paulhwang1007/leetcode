# Last updated: 12/19/2025, 10:11:44 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        res = 0
4        l, r = 0, len(height) - 1
5
6        while l < r:
7            area = (r - l) * min(height[l], height[r])
8            res = max(res, area)
9
10            if height[l] < height[r]:
11                l += 1
12            else:
13                r -= 1
14        return res