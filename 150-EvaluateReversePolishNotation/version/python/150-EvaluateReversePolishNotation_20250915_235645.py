# Last updated: 9/15/2025, 11:56:45 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Rules:
        # Only add open if open < n
        # Only add closed if closed < open
        # Valid iif open == closed == n
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res