class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        minheap=[]
        heapq.heappush(minheap,(0,0,0))
        visited=set()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        while minheap:
            effort,r,c=heapq.heappop(minheap)

            if (r,c) in visited:
                continue
                
            visited.add((r,c))

            if r==m-1 and c==n-1:
                return effort

            for dr,dc in directions:
                x=dr+r
                y=dc+c
                if x<0 or x>m-1 or y<0 or y>n-1 or (x,y) in visited:
                    continue
                maxeffort=max(effort,abs(heights[x][y]-heights[r][c]))
                heapq.heappush(minheap,(maxeffort,x,y))   
        return -1