class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for op in ops:
            if stack and op=="+":
                first=stack[-1]
                second=stack[-2]
                stack.append(first+second)
            elif stack and op=="D":
                first=stack[-1]
                stack.append(first*2)
            elif stack and op=="C":
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)