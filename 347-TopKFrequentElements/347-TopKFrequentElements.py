# Last updated: 7/26/2026, 3:53:11 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for i in range(len(nums) + 1)]
        res = []

        # count frequencies
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        # append into buckets
        for num, freq in freq.items():
            buckets[freq].append(num)

        # iterate through buckets
        for bucket in range(len(buckets) - 1, 0, -1):
            for num in buckets[bucket]:
                res.append(num)
                if len(res) == k:
                    return res
