class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for ast in asteroids:
            alive=True

            while stack and stack[-1]>0 and ast<0:

                if abs(stack[-1])>abs(ast):
                    alive=False
                    break
                
                elif abs(stack[-1])==abs(ast):
                    stack.pop()
                    alive=False
                    break
                
                else:
                    stack.pop()
                    
            if alive:
                stack.append(ast)
        return stack

