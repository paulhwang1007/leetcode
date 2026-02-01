# Last updated: 2/1/2026, 1:33:42 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        freq = {}
4        buckets = [[] for i in range(len(nums) + 1)]
5        res = []
6
7        # count frequencies
8        for num in nums:
9            if num not in freq:
10                freq[num] = 0
11            freq[num] += 1
12        
13        # append into buckets
14        for num, freq in freq.items():
15            buckets[freq].append(num)
16
17        # iterate through buckets
18        for bucket in range(len(buckets) - 1, 0, -1):
19            for num in buckets[bucket]:
20                res.append(num)
21                if len(res) == k:
22                    return res
23