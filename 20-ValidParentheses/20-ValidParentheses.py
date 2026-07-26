# Last updated: 7/26/2026, 3:53:39 PM
class Solution:
    def isValid(self, s: str) -> bool:
        paren = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char in paren:
                if not stack or paren[char] != stack[-1]:
                    return False
                else: 
                    stack.pop()
            else:
                stack.append(char)
        return not stack

