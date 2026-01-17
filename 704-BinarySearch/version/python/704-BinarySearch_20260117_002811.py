# Last updated: 1/17/2026, 12:28:11 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left <= right:
6            mid = (left + right) // 2
7
8            if nums[mid] > target:
9                right = mid - 1
10            elif nums[mid] < target:
11                left = mid + 1
12            else:
13                return mid
14        return -1