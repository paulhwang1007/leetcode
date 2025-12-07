# Last updated: 12/6/2025, 11:08:29 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        paren = {")":"(", "}":"{", "]":"["}
4        stack = []
5
6        for char in s:
7            if char in paren:
8                if len(stack) != 0 and paren[char] == stack[-1]:
9                    stack.pop()
10                else:
11                    return False
12            else:
13                stack.append(char)        
14        return not stack