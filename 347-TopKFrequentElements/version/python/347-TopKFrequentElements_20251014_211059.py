# Last updated: 10/14/2025, 9:10:59 PM
class Solution:
    def isValid(self, s: str) -> bool:
        paren = {"(":")", "[":"]", "{":"}"}
        stack = []

        for char in s:
            if char in paren:
                stack.append(char)
            elif len(stack) == 0 or paren[stack.pop()] != char:
                return False
        return len(stack) == 0
