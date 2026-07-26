# Last updated: 7/26/2026, 3:53:06 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for char in s1:
            if char not in s1_freq:
                s1_freq[char] = 0
            s1_freq[char] += 1
        
        l, r = 0, len(s1) - 1
        while r <= len(s2):
            s2_freq = {}
            for char in s2[l:r+1]:
                if char not in s2_freq:
                    s2_freq[char] = 0
                s2_freq[char] += 1
            
            if s2_freq == s1_freq:
                return True
            else:
                s2_freq = {}
                l += 1
                r += 1
        return False