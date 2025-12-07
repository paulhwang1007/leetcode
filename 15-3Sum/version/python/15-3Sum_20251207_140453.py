# Last updated: 12/7/2025, 2:04:53 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        arr = []
4        nums.sort()
5
6        for i, val in enumerate(nums):
7            if i > 0 and val == nums[i-1]:
8                continue
9            
10            j, k = i + 1, len(nums) - 1
11            while j < k:
12                sum = val + nums[j] + nums[k]
13                if sum > 0:
14                    k -= 1
15                elif sum < 0:
16                    j += 1
17                else:
18                    arr.append([val, nums[j], nums[k]])
19                    j += 1
20                    while nums[j] == nums[j-1] and j < k:
21                        j += 1
22        return arr