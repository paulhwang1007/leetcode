# Last updated: 7/26/2026, 3:53:03 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = right

        while left <= right:
            hours = 0
            mid = (left + right) // 2

            for i in piles:
                hours += math.ceil(i / mid)

            if hours <= h:
                min_k = min(min_k, mid)
                right = mid - 1
            else:
                left = mid + 1

        return min_k
            

        