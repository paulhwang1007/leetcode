# Last updated: 12/7/2025, 1:52:12 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left, right = 1, len(numbers)
4
5        for i in numbers:
6            sum = numbers[left-1] + numbers[right-1]
7
8            if sum == target:
9                return [left, right]
10            elif sum > target:
11                right -= 1
12            elif sum < target:
13                left += 1