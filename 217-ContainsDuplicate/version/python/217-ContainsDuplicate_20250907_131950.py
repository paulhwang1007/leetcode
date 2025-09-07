# Last updated: 9/7/2025, 1:19:50 PM
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

        