class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for op in ops:
            if stack and op=="+":
                first=int(stack[-1])
                second=int(stack[-2])
                stack.append(int(first+second))
            elif stack and op=="D":
                first=int(stack[-1])
                stack.append(int(first*2))
            elif stack and op=="C":
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)