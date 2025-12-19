# Last updated: 12/18/2025, 8:58:22 PM
1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        temp = sorted(nums)
4        d = {}
5
6        for i, num in enumerate(temp):
7            if num not in d:
8                d[num] = i
9        
10        ret = []
11
12        for i in nums:
13            ret.append(d[i])
14        
15        return ret