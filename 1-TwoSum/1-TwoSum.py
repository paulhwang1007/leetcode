# Last updated: 8/1/2026, 1:26:21 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hash = {}
4
5        for i in range(len(nums)):
6            diff = target - nums[i]
7            if diff in hash:
8                return [hash[diff], i]
9            else:
10                hash[nums[i]] = i