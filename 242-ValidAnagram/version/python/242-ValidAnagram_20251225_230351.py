# Last updated: 12/25/2025, 11:03:51 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        groups = {}
4
5        for string in strs:
6            chars = ''.join(sorted(string))
7
8            if chars not in groups:
9                groups[chars] = [string]
10            else:
11                groups[chars].append(string)
12        return list(groups.values())