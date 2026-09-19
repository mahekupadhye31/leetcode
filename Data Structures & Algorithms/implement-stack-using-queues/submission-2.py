class MyStack:
    #q1=[]
    #q2=[]

    # push 1
    # q1=[]
    # q2=[1]

    # now swap

    # q1=[1]
    # q2=[]

    # push 2

    # q1=[1]
    # q2=[2]

    # while q1 exists

    # q1=[]
    # q2=[2,1]

    # now swap

    # q1=[2,1]
    # q2=[]

    # push 3

    # q1=[2,1]
    # q2=[3]

    # while q1 exists

    # q1=[]
    # q2=[3,2,1]

    # now swap

    # q1=[3,2,1]
    # q2=[]

    # push 4

    # q1=[3,2,1]
    # q2=[4]

    # while q1 exists

    # q1=[]
    # q2=[4,3,2,1]

    # now swap

    # q1=[4,3,2,1]
    # q2=[]

    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return True if len(self.q1)==0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()