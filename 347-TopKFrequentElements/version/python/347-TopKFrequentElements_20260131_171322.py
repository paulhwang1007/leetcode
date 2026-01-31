# Last updated: 1/31/2026, 5:13:22 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        res = []
4        anagrams = {}
5
6        for string in strs:
7            letters_list = sorted(string)
8            letters = "".join(letters_list)
9
10            if letters not in anagrams:
11                anagrams[letters] = []
12
13            anagrams[letters].append(string)
14        
15        for val in anagrams.values():
16            res.append(val)
17        
18        return res