# Last updated: 12/19/2025, 12:39:46 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        nums.sort()
5
6        for i, val in enumerate(nums):
7            # deal with dupes for i
8            if i > 0 and val == nums[i - 1]:
9                continue
10            
11            # opposite direction two pointer for j and k
12            # the for loop iterates over i
13            j, k = i + 1, len(nums) - 1
14            while j < k:
15                sum = val + nums[j] + nums[k]
16                if sum > 0:
17                    k -= 1
18                elif sum < 0:
19                    j += 1
20                else:
21                    res.append([val, nums[j], nums[k]])
22                    j += 1
23                    # deal with dupes for j
24                    while nums[j] == nums[j - 1] and j < k:
25                        j += 1
26        return res
27