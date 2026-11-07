class MinStack:
    def __init__(self):
        self.minstack=[]
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal=val
        if self.minstack:
            minVal=min(val,self.minstack[-1])
        self.minstack.append(minVal)

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]