# Last updated: 10/10/2025, 3:08:35 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            letters = "".join(sorted(word))
            
            if letters not in groups:
                groups[letters] = []
            
            groups[letters].append(word)
        
        return list(groups.values())
