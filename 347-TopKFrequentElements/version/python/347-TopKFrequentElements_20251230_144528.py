# Last updated: 12/30/2025, 2:45:28 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums = set(nums)
4        longest = 0
5
6        for num in nums:
7            if (num - 1) not in nums:
8                length = 0
9                while (num + length) in nums:
10                    length += 1
11                longest = max(longest, length)
12        return longest
13