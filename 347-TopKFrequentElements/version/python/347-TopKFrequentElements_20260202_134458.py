# Last updated: 2/2/2026, 1:44:58 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        stack = []
4        abs_path = path.split("/")
5
6        for file in abs_path:
7            if file == "" or file == ".":
8                continue
9            elif file == "..":
10                if stack:
11                    stack.pop()
12            else:
13                stack.append(file)
14        
15        smple_path = "/" + "/".join(stack)
16        return smple_path