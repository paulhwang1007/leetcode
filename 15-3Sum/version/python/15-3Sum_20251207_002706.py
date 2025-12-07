# Last updated: 12/7/2025, 12:27:06 AM
class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list=path.split('/')
        print(dir_list)
        stack=[]
        for i in dir_list:
            if i =='.' or i=='':
                continue
            elif  i=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/"+'/'.join(stack)