# Last updated: 12/6/2025, 10:05:11 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        nums.sort()
5
6        for i, a in enumerate(nums):
7            if i > 0 and a == nums[i - 1]:
8                continue
9            
10            j, k = i + 1, len(nums) - 1
11            while j < k:
12                sum = a + nums[j] + nums[k]
13                if sum > 0:
14                    k -= 1
15                elif sum < 0:
16                    j += 1
17                else:
18                    res.append([a, nums[j], nums[k]])
19                    j += 1
20                    while nums[j] == nums[j - 1] and j < k:
21                        j += 1
22        return res