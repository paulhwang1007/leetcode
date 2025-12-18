# Last updated: 12/18/2025, 6:20:05 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        pairs = {}
4
5        for i in range(len(nums)):
6            diff = target - nums[i]
7
8            if diff in pairs:
9                return [i, pairs[diff]]
10            else:
11                pairs[nums[i]] = i
12                # nums[i]: i