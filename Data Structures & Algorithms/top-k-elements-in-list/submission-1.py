class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        result=[]

        for num in nums:
            h[num]=1+h.get(num,0)

        minheap=[]
        for key,value in h.items():
            heapq.heappush(minheap,(value,key))
            if len(minheap)>k:
                heapq.heappop(minheap)
        
        while minheap:
            val,key=heapq.heappop(minheap)
            result.append(key)
        return result