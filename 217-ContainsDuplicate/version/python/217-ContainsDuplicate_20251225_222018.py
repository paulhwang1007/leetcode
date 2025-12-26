# Last updated: 12/25/2025, 10:20:18 PM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        unique = set(nums)
8
9        return len(unique) != len(nums)
10