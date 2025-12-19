# Last updated: 12/18/2025, 7:51:42 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        nums.sort()
4        for i, v in enumerate(nums):
5            if i != v:
6                return v-1
7            if v == (len(nums) - 1):
8                return v+1