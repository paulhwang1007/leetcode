# Last updated: 7/30/2026, 10:45:00 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left, right = 1, len(numbers)
4
5        while left < right:
6            sum = numbers[left - 1] + numbers[right - 1]
7            if sum == target:
8                return [left, right]
9            elif sum < target:
10                left += 1
11            else:
12                right -= 1