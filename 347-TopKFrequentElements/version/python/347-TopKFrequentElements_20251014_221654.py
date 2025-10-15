# Last updated: 10/14/2025, 10:16:54 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token == "+":
                num1, num2 = int(stack.pop()), int(stack.pop())
                stack.append(num1 + num2)
            elif token == "-":
                num1, num2 = int(stack.pop()), int(stack.pop())
                stack.append(num2 - num1)
            elif token == "*":
                num1, num2 = int(stack.pop()), int(stack.pop())
                stack.append(num1 * num2)
            elif token == "/":
                num1, num2 = int(stack.pop()), int(stack.pop())
                stack.append(num2 / num1)
            else:
                stack.append(int(token))

        return int(stack[-1])