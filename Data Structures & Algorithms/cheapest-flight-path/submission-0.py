class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for s,d,c in flights:
            adj[s].append((d,c))
        
        # visited=set()
        minheap=[]
        heapq.heappush(minheap,(0,src,0))
        distance=[float('inf') for _ in range(n)]
        distance[src]=0

        while minheap:
            stops,node,dist=heapq.heappop(minheap)
            if stops>k:
                continue
            for nei,cost in adj[node]:
                if dist+ cost< distance[nei]:
                    heapq.heappush(minheap,(stops+1,nei,dist+cost))
                    distance[nei]=dist+cost
        
        return distance[dst] if distance[dst]!=float('inf') else -1