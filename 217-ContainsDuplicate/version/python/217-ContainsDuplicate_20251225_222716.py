# Last updated: 12/25/2025, 10:27:16 PM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        frequency = {}
8        nums.sort() # sorts nums in ascending order
9
10        for num in nums:
11            if num not in frequency:
12                frequency[num] = 1
13            else:
14                return True
15        
16        return False
17