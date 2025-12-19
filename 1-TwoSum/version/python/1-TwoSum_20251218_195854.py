# Last updated: 12/18/2025, 7:58:54 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        return sum(range(len(nums)+1)) - sum(nums)