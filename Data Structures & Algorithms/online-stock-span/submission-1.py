class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        count=1

        # if len(self.stack)==0:
        #     self.stack.append(price)

        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i]<=price:
                count+=1
            else:
                break
        self.stack.append(price)
        return count
      
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)