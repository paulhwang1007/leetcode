# Last updated: 12/8/2025, 12:38:57 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        left, right = 1, max(piles)
4        min_k = right
5
6        while left <= right:
7            hours = 0
8            mid = (left + right) // 2
9
10            for i in piles:
11                hours += math.ceil(i / mid)
12
13            if hours <= h:
14                min_k = min(min_k, mid)
15                right = mid - 1
16            else:
17                left = mid + 1
18
19        return min_k
20            
21
22        