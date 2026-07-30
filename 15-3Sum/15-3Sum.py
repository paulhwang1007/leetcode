# Last updated: 7/30/2026, 11:10:19 AM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        triplets = []
4        nums.sort()
5
6        i = 0
7
8        for i, num in enumerate(nums):
9            
10            # if duplicate, go to the next pass
11            if i > 0 and num == nums[i - 1]:
12                continue
13
14            j, k = i + 1, len(nums) - 1
15            while j < k:
16                sum = nums[i] + nums[j] + nums[k]
17                if sum < 0:
18                    j += 1
19                elif sum > 0:
20                    k -= 1
21                else:
22                    triplets.append([nums[i], nums[j], nums[k]])
23                    j += 1
24                    while nums[j] == nums[j - 1] and j < k:
25                        j += 1
26        
27        return triplets