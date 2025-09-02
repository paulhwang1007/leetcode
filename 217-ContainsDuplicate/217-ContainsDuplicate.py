# Last updated: 9/2/2025, 5:14:23 PM
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return len(set(nums)) != len(nums)