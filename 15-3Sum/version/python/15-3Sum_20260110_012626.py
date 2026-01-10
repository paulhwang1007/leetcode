# Last updated: 1/10/2026, 1:26:26 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        nums.sort()
5
6        for i, num in enumerate(nums):
7            if i > 0 and num == nums[i-1]:
8                continue
9            
10            j, k = i + 1, len(nums) - 1
11
12            while j < k:
13                sum = num + nums[j] + nums[k]
14
15                if sum > 0:
16                    k -= 1
17                elif sum < 0:
18                    j += 1
19                else:
20                    res.append([num, nums[j], nums[k]])
21                    j += 1
22                    while nums[j] == nums[j-1] and j < k:
23                        j += 1
24            
25        return res
26                    
27