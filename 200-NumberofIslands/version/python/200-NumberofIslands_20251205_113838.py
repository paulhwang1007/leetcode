# Last updated: 12/5/2025, 11:38:38 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = 0
4        seen = {}
5        max_length = 0
6
7        for right in range(len(s)):
8            if s[right] not in seen:
9                seen[s[right]] = 0
10            seen[s[right]] += 1
11
12            while seen[s[right]] > 1:
13                seen[s[left]] -= 1
14                left += 1
15
16            max_length = max(max_length, right - left + 1)
17        
18        return max_length
19            