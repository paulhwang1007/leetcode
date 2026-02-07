# Last updated: 2/7/2026, 5:29:16 PM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        freq = {}
8
9        for num in nums:
10            if num not in freq:
11                freq[num] = 0
12            freq[num] += 1
13
14            if freq[num] > 1:
15                return True
16        return False