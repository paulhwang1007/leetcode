# Last updated: 10/7/2025, 9:35:38 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hash:
                return [i, hash[pair]]
            hash[nums[i]] = i

            
                

            