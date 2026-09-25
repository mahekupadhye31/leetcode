class FreqStack:

    def __init__(self):
        self.hashmap={}
        self.maxcount=0
        self.groups=defaultdict(list)
        

    def push(self, val: int) -> None:
        newval=1+self.hashmap.get(val,0)
        self.hashmap[val]=newval
        if newval>self.maxcount:
            self.maxcount=newval
        self.groups[newval].append(val)
        
    def pop(self) -> int:
        res=self.groups[self.maxcount].pop()
        self.hashmap[res]-=1
        if len(self.groups[self.maxcount])==0:
            self.maxcount-=1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()