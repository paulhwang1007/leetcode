# Last updated: 7/28/2026, 11:38:16 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        freq = {}
4        buckets = [[] for i in range(len(nums) + 1)]
5        topK = []
6
7        # get frequencies
8        # { num: freq }
9        for num in nums:
10            if num not in freq:
11                freq[num] = 0
12            freq[num] += 1
13        
14        # append numbers to bucket
15        for num, count in freq.items():
16            buckets[count].append(num)
17        
18        # return top k
19        for bucket in range(len(buckets) - 1, 0, -1):
20            for num in buckets[bucket]:
21                topK.append(num)
22
23                if len(topK) == k:
24                    return topK