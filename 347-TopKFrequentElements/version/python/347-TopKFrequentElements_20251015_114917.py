# Last updated: 10/15/2025, 11:49:17 AM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        curr = []

        def backtrack(numOpen: int, numClose: int):
            if numOpen == numClose == n:
                final.append("".join(curr))
                return

            if numOpen < n:
                curr.append("(")
                backtrack(numOpen + 1, numClose)
                curr.pop()
                
            if numClose < numOpen:
                curr.append(")")
                backtrack(numOpen, numClose + 1)
                curr.pop()
        
        backtrack(0, 0)
        return final