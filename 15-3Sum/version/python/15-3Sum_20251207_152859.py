# Last updated: 12/7/2025, 3:28:59 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack = []
4
5        for i in range(len(s)):
6            if s[i] != "]":
7                stack.append(s[i])
8            else:
9                substr = ""
10                while stack[-1] != "[":
11                    substr = stack.pop() + substr
12                stack.pop()
13
14                k = ""
15                while stack and stack[-1].isdigit():
16                    k = stack.pop() + k
17                
18                stack.append(int(k) * substr)
19        return "".join(stack)
20