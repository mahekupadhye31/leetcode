class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        
    def push(self, val: int) -> None:
        if len(self.minstack)==0:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1],val))
        self.stack.append(val)
           
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        