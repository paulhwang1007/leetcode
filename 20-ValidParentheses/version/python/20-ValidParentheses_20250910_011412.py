# Last updated: 9/10/2025, 1:14:12 AM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opt = {"(":")", "{":"}", "[":"]"}
        stack = []

        for i in s:
            if i in opt:
                stack.append(i)
            elif len(stack) == 0 or opt[stack.pop()] != i:
                return False
        return len(stack) == 0