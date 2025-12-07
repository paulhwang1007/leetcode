# Last updated: 12/7/2025, 12:26:21 AM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        stack = []
4        string = ""
5
6        for char in path + "/":
7            if char == "/":
8                if string == "..":
9                    if stack:
10                        stack.pop()
11                elif string != "" and string != ".":
12                    stack.append(string)
13                string = ""
14            else:
15                string += char
16        return "/" + "/".join(stack)