class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        minheap=[]
        for key,value in count.items():
            heapq.heappush(minheap,(value,key))
            if len(minheap)>k:
                heapq.heappop(minheap)
        while minheap:
            count,num= heapq.heappop(minheap)
            res.append(num)
        return res