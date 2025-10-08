# Last updated: 10/7/2025, 9:14:34 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s, hash_t = {}, {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter in hash_s:
                hash_s[letter] += 1
            else:
                hash_s[letter] = 1
        for letter in t:
            if letter in hash_t:
                hash_t[letter] += 1
            else:
                hash_t[letter] = 1
        
        if hash_s == hash_t:
            return True
        return False