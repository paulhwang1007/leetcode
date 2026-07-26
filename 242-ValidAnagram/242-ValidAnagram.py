# Last updated: 7/26/2026, 3:53:13 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for letter in s:
            if letter not in hash_s:
                hash_s[letter] = 0
            hash_s[letter] += 1
        
        for letter in t:
            if letter not in hash_t:
                hash_t[letter] = 0
            hash_t[letter] += 1
        
        return hash_s == hash_t