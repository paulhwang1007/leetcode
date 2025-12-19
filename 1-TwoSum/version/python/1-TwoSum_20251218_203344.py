# Last updated: 12/18/2025, 8:33:44 PM
1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        missing = []
4        set_nums = set(nums)
5
6        for i in range(1, len(nums) + 1):
7            if i not in set_nums:
8                missing.append(i)
9        return missing