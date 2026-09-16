class MedianFinder:
    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        maxheaptop = -heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, maxheaptop)

        # FIX: this second block is what was entirely missing.
        # The block above unconditionally moves the new number's
        # rightful spot into minheap first — simplest way to guarantee
        # every value passes through maxheap's ordering check once.
        # Now correct the balance, in WHICHEVER direction it's off:
        if len(self.minheap) > len(self.maxheap):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)

        
    def findMedian(self) -> float:
        if len(self.maxheap)>len(self.minheap):
            return -self.maxheap[0]
        elif len(self.maxheap)<len(self.minheap):
            return self.minheap[0]
        else:
            return (self.minheap[0]+ (-self.maxheap[0]))/2