# Last updated: 12/8/2025, 1:55:37 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left <= right:
6            mid = (left + right) // 2
7
8            if nums[mid] == target:
9                return mid
10            elif nums[mid] > target:
11                right = mid - 1
12            else:
13                left = mid + 1
14        return -1
15