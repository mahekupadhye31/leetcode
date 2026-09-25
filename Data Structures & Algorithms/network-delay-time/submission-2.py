class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList=defaultdict(list)
        for s,d,c in times:
            adjList[s].append((d,c))
        
        distances=[float("inf")]*(n+1)
        distances[0]=-1
        distances[k]=0

        minheap=[]
        heapq.heappush(minheap,(k,0))

        while minheap:
            node,dist=heapq.heappop(minheap)
            for nei,c in adjList[node]:
                if distances[nei]>dist+c:
                    distances[nei]=dist+c
                    heapq.heappush(minheap,(nei,dist+c))
        

        return max(distances) if max(distances)!=float("inf") else -1