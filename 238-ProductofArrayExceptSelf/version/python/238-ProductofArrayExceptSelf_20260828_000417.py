# Last updated: 8/28/2026, 12:04:17 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        result = [1] * n
5
6        # Prefix Pass
7        prefix = 1
8        for i in range(n):
9            result[i] = prefix
10            prefix *= nums[i]
11        
12        # Postfix Pass
13        postfix = 1
14        for i in range(n-1, -1, -1):
15            result[i] *= postfix
16            postfix *= nums[i]
17        
18        return result