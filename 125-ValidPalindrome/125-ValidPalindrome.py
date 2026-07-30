# Last updated: 7/30/2026, 12:06:58 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        lower = s.lower()
4        string = "".join(char for char in lower if char.isalnum())
5
6        start, end = 0, len(string) - 1
7
8        while start <= end:
9            if string[start] != string[end]:
10                return False
11            start += 1
12            end -= 1
13        return True