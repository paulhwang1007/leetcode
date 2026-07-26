# Last updated: 7/26/2026, 3:53:18 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)

        for i in numbers:
            sum = numbers[left-1] + numbers[right-1]

            if sum == target:
                return [left, right]
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1