# Last updated: 12/25/2025, 10:40:15 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s_count = {}
4        t_count = {}
5
6        for char in s:
7            if char not in s_count:
8                s_count[char] = 1
9            else:
10                s_count[char] += 1
11        
12        for char in t:
13            if char not in t_count:
14                t_count[char] = 1
15            else:
16                t_count[char] += 1
17        
18        return s_count == t_count