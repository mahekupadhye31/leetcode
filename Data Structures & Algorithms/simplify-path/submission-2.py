class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        directories=path.split('/')

        for p in directories:
            if p==" " or p=="" or p==".":
                continue
            elif p=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(p) 
        
        return "/" + "/".join(stack) if len(stack)!=0 else "/"
