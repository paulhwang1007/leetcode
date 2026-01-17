# Last updated: 1/17/2026, 12:17:19 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if t == "": return ""
4
5        countT, window = {}, {}
6
7        for c in t:
8            countT[c] = 1 + countT.get(c, 0)
9        
10        have, need = 0, len(countT)
11        res, resLen = [-1, -1], float('infinity')
12        l = 0
13
14        for r in range(len(s)):
15            c = s[r]
16            window[c] = 1 + window.get(c, 0)
17
18            if c in countT and window[c] == countT[c]:
19                have += 1
20            
21            while have == need:
22                if (r - l + 1) < resLen:
23                    res = [l, r]
24                    resLen = (r - l + 1)
25                
26                window[s[l]] -= 1
27                if s[l] in countT and window[s[l]] < countT[s[l]]:
28                    have -= 1
29                
30                l += 1
31        
32        l, r = res
33        return s[l:r+1] if resLen != float("infinity") else ""
34