# Last updated: 12/6/2025, 11:05:30 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        options = {"(":")", "{":"}", "[":"]"}
4        stack = []
5
6        for char in s:
7            if char in options:
8                stack.append(char)
9            elif len(stack) == 0 or options[stack.pop()] != char:
10                return False
11        return len(stack) == 0