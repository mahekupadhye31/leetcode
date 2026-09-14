class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for s,d,time in times:
            adj[s].append((d,time))
        
        minheap=[]
        distance=[float('inf') for _ in range(n+1)]
        heapq.heappush(minheap,(0,k))
        distance[k]=0

        while minheap:
            time,node=heapq.heappop(minheap)
            for nei,t in adj[node]:
                if (time+t)<distance[nei]:
                    distance[nei]=time+t
                    heapq.heappush(minheap,(time+t,nei))

        maxi = float('-inf');
        for i in range(1,len(distance)):
            if distance[i]==float('inf'):
                return -1
            elif distance[i] > maxi:
                maxi = distance[i]
            
        return maxi

        