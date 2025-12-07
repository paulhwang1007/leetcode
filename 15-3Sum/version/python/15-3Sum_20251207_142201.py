# Last updated: 12/7/2025, 2:22:01 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        letters = set()
4        left = 0
5        length = 0
6
7        for right in range(len(s)):
8            while s[right] in letters:
9                letters.remove(s[left])
10                left += 1
11            letters.add(s[right])
12            length = max(length, right - left + 1)
13        return length