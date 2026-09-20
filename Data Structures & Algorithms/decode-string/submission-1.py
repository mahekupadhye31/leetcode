class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]=="]":
                temp=""
                while stack[-1]!="[":
                    temp=stack.pop() + temp
                stack.pop() #for the opening square bracket
                number=""
                while stack and stack[-1].isdigit():
                    number=stack.pop()+number

                temp=temp*int(number)
                stack.append(temp)
            else:
                stack.append(s[i])
        return "".join(stack)