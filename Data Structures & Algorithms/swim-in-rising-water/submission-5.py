class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap=[]
        m=len(grid)
        n=len(grid[0])
        heapq.heappush(minheap,(grid[0][0],0,0))
        visited=set()
        #stores max time taken, row, col
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        while minheap:
            time,r,c=heapq.heappop(minheap)
            if (r,c) in visited:
                continue

            visited.add((r,c))

            if r==m-1 and c==n-1:
                return time
            for dr, dc in directions:
                x=dr+r
                y=dc+c
                if x<0 or x>m-1 or y<0 or y>n-1 or (x,y) in visited:
                    continue
                heapq.heappush(minheap,(max(grid[x][y],time),x,y))
                grid[x][y]= max(grid[x][y],time)      
        return 0          