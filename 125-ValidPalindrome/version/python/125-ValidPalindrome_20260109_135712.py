# Last updated: 1/9/2026, 1:57:12 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s_lower = s.lower()
4        s = ''.join(char for char in s_lower if char.isalnum())
5
6        i, j = 0, len(s) - 1
7
8        if len(s) == 0:
9            return True
10
11        while i <= j:
12            if s[i] != s[j]:
13                return False
14            i += 1
15            j -= 1
16        return True
17            