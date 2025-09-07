# Last updated: 9/7/2025, 1:02:20 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            addend = target - nums[i]
            if addend in hash:
                return [i, hash[addend]]
            else:
                hash[nums[i]] = i