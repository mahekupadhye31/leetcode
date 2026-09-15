class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[]
        for stone in stones:
            heapq.heappush(maxheap,(-stone))
        
        while len(maxheap)>1:
            x=abs(heapq.heappop(maxheap))
            y=abs(heapq.heappop(maxheap))
            if x==y:
                continue
            elif abs(x)<abs(y):
                heapq.heappush(maxheap,-(abs(y)-abs(x)))
            else:
                heapq.heappush(maxheap,-(abs(x)-abs(y)))
        
        return abs(maxheap[0]) if maxheap else 0