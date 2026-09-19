class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for ast in asteroids:
            while stack and stack[-1]>0 and ast<0:
                if stack[-1]==abs(ast):
                    ast=0
                    stack.pop()
                    break
                if stack[-1]>abs(ast):
                    ast=0
                    break
                if stack[-1]<abs(ast):
                    stack.pop()
            
            if ast!=0:
                # stack.pop()
                stack.append(ast)
        return stack

# [10,2,-5]
# 10, 2, 