# Last updated: 7/26/2026, 3:53:02 PM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}

        for i, num in enumerate(temp):
            if num not in d:
                d[num] = i
        
        ret = []

        for i in nums:
            ret.append(d[i])
        
        return ret