class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap=[]
        result=[]
        if not points:
            return
        for x,y in points:
            distance=(x**2+y**2)**0.5
            heapq.heappush(maxheap,(-distance,[x,y]))
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        
        while maxheap:
            dist, point=heapq.heappop(maxheap)
            result.append(point)
        return result
