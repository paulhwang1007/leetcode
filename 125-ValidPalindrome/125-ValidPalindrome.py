# Last updated: 7/26/2026, 3:53:25 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s = ''.join(char for char in s_lower if char.isalnum())

        i, j = 0, len(s) - 1

        if len(s) == 0:
            return True

        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            