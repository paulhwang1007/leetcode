# Last updated: 8/11/2026, 10:42:08 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4
5        for token in tokens:
6            if token == "+":
7                second, first = int(stack.pop()), int(stack.pop())
8                res = first + second
9                stack.append(res)
10            elif token == "-":
11                second, first = int(stack.pop()), int(stack.pop())
12                res = first - second
13                stack.append(res)
14            elif token == "*":
15                second, first = int(stack.pop()), int(stack.pop())
16                res = first * second
17                stack.append(res)
18            elif token == "/":
19                second, first = int(stack.pop()), int(stack.pop())
20                res = first / second
21                stack.append(res)
22            else:
23                stack.append(int(token))
24        return int(stack.pop())