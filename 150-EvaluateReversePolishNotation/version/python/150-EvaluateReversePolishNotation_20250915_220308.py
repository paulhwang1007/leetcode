# Last updated: 9/15/2025, 10:03:08 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operators:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                match token:
                    case "+":
                        result = op1 + op2
                    case "-":
                        result = op1 - op2
                    case "*":
                        result = op1 * op2
                    case "/":
                        result = op1 / op2
                stack.append(result)
            else:
                stack.append(token)
        return int(stack.pop())
        
