# Last updated: 12/7/2025, 1:24:13 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        stack = []
4        abs_path = path.split("/")
5
6        for char in abs_path:
7            if char == "" or char == ".":
8                continue
9            elif char == "..":
10                if stack:
11                    stack.pop()
12            else:
13                stack.append(char)
14        return "/" + "/".join(stack)