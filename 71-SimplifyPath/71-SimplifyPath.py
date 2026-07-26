# Last updated: 7/26/2026, 3:53:33 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        abs_path = path.split("/")

        for file in abs_path:
            if file == "" or file == ".":
                continue
            elif file == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(file)
        
        smple_path = "/" + "/".join(stack)
        return smple_path