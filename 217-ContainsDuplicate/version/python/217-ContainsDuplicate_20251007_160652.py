# Last updated: 10/7/2025, 4:06:52 PM
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        freq = {}
        for num in nums:
            if num in freq:
                return True
            else:
                freq[num] = 1
        return False