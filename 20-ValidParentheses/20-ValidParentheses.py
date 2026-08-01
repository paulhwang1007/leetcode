# Last updated: 8/1/2026, 1:26:37 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        brackets = { "(": ")", "{": "}", "[": "]" }
4        stack = []
5
6        for bracket in s:
7            if bracket in brackets:
8                stack.append(bracket)
9            elif len(stack) == 0 or brackets[stack.pop()] != bracket:
10                return False
11        return len(stack) == 0
12