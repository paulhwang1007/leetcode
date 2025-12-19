# Last updated: 12/19/2025, 10:49:21 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        res = ""
4        resLen = 0
5
6        for i in range(len(s)):
7            # odd length
8            l, r = i, i
9            while l >= 0 and r < len(s) and s[l] == s[r]:
10                if (r - l + 1) > resLen:
11                    res = s[l:r+1]
12                    resLen = r - l + 1
13                l -= 1
14                r += 1
15            
16            # even length
17            l, r = i, i + 1
18            while l >= 0 and r < len(s) and s[l] == s[r]:
19                if (r - l + 1) > resLen:
20                    res = s[l:r+1]
21                    resLen = r - l + 1
22                l -= 1
23                r += 1
24        
25        return res