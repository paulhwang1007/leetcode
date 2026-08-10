# Last updated: 8/9/2026, 11:16:29 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        brackets = { "{": "}", "[": "]", "(": ")" }
4        stack = []
5
6        for bracket in s:
7            if bracket in brackets:
8                stack.append(bracket)
9            else:
10                if len(stack) == 0 or brackets[stack.pop()] != bracket:
11                    return False
12        
13        return len(stack) == 0