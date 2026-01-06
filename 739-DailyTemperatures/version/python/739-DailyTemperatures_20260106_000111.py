# Last updated: 1/6/2026, 12:01:11 AM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        maxArea = 0
4        stack = [] # index, height
5
6        for i, h in enumerate(heights):
7            start = i
8            while stack and stack[-1][1] > h:
9                index, height = stack.pop()
10                maxArea = max(maxArea, height * (i - index))
11                start = index
12            stack.append((start, h))
13
14        for i, h in stack:
15            maxArea = max(maxArea, h * (len(heights) - i))
16        
17        return maxArea