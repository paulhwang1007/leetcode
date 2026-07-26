# Last updated: 7/26/2026, 3:53:44 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        max_length = 0

        i = 0

        for j in range(len(s)):
            if s[j] not in hash:
                hash[s[j]] = 0
            hash[s[j]] += 1

            while hash[s[j]] > 1:
                hash[s[i]] -= 1
                i += 1
            
            max_length = max(max_length, j - i + 1)

        return max_length
