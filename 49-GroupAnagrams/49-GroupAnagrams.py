# Last updated: 7/27/2026, 9:15:08 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        hash = {}
4
5        for string in strs:
6            letters_list = sorted(string)
7            letters = "".join(letters_list)
8            
9            if letters not in hash:
10                hash[letters] = [string]
11            else:
12                hash[letters].append(string)
13        
14        return list(hash.values())