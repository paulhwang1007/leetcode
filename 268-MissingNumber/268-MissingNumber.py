# Last updated: 7/26/2026, 3:53:12 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)