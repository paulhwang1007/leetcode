# Last updated: 10/14/2025, 10:18:30 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                op1, op2 = stack.pop(), stack.pop()
                stack.append(op2 - op1)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                op1, op2 = stack.pop(), stack.pop()
                stack.append(int(op2 / op1))
            else:
                stack.append(int(c))
        return stack[0]