# Last updated: 12/5/2025, 3:16:38 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left, right = 1, len(numbers)
4
5        while left < right:
6            sum = numbers[left - 1] + numbers[right - 1]
7
8            if sum == target:
9                return [left, right]
10            elif sum > target:
11                right -= 1
12            else:
13                left += 1