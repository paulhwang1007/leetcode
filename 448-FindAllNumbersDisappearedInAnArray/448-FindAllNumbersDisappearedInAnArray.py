# Last updated: 7/26/2026, 3:53:07 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []
        set_nums = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                missing.append(i)
        return missing