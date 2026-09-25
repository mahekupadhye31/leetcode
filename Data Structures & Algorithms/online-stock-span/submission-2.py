class StockSpanner:

    def __init__(self):
        self.stack=[]
    
    def next(self, price: int) -> int:
        self.count=1

        if len(self.stack)==0:
            self.stack.append(price)
            return 1

        length=len(self.stack)

        for i in range(length-1,-1,-1):
            if price>=self.stack[i]:
                self.count+=1
            else:
                break
        self.stack.append(price)
        return self.count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)