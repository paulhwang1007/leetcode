# Last updated: 1/15/2026, 11:02:10 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        s1_freq = {}
4        for char in s1:
5            if char not in s1_freq:
6                s1_freq[char] = 0
7            s1_freq[char] += 1
8        
9        l, r = 0, len(s1) - 1
10        while r <= len(s2):
11            s2_freq = {}
12            for char in s2[l:r+1]:
13                if char not in s2_freq:
14                    s2_freq[char] = 0
15                s2_freq[char] += 1
16            
17            if s2_freq == s1_freq:
18                return True
19            else:
20                s2_freq = {}
21                l += 1
22                r += 1
23        return False