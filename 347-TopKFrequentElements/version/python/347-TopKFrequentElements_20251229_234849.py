# Last updated: 12/29/2025, 11:48:49 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        res = [1] * len(nums)
4        prefix, postfix = 1, 1
5
6        for i in range(len(nums)):
7            res[i] = prefix
8            prefix *= nums[i]
9        
10        for i in range(len(nums) - 1, -1, -1):
11            res[i] *= postfix
12            postfix *= nums[i]
13        
14        return res