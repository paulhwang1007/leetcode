# Last updated: 10/16/2025, 1:47:08 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        clean_s = ''.join(char for char in s_lower if char.isalnum())

        if len(clean_s) == 0:
            return True

        start, end = 0, len(clean_s) - 1

        while start <= end:
            if clean_s[start] != clean_s[end]:
                return False
            
            start += 1
            end -= 1

        return True