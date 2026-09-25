class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minheap=[]
        heapq.heappush(minheap,(0,0,src))
        distances=[float("inf")]*n
        distances[src]=0
        visited=set()
        adj=defaultdict(list)
        for s,d,cost in flights:
            adj[s].append((d,cost))

        while minheap:
            stops,cost,node=heapq.heappop(minheap)
            # if node in visited:
            #     continue
            # visited.add(node)
            if stops>k:
                continue
            for nei,exp in adj[node]:
                if distances[nei]>cost+exp:
                    distances[nei]=cost+exp
                    heapq.heappush(minheap,(stops+1,distances[nei],nei))
        return distances[dst] if distances[dst]!=float("inf") else -1

            