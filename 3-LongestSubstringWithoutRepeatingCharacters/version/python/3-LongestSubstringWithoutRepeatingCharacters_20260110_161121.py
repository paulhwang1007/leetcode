# Last updated: 1/10/2026, 4:11:21 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        hash = {}
4        max_length = 0
5
6        i = 0
7
8        for j in range(len(s)):
9            if s[j] not in hash:
10                hash[s[j]] = 0
11            hash[s[j]] += 1
12
13            while hash[s[j]] > 1:
14                hash[s[i]] -= 1
15                i += 1
16            
17            max_length = max(max_length, j - i + 1)
18
19        return max_length
20