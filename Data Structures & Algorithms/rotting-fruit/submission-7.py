class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])
        visited=set()
        q=deque()
        fresh=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    visited.add((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        maxTime=0
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            r,c,time=q.popleft()
            maxTime=max(maxTime,time)
            for dr,dc in directions:
                x=dr+r
                y=dc+c
                if (x<0 or x>m-1 or y<0 or y>n-1 or (x,y) in visited or grid[x][y]==0):
                    continue

                grid[x][y]=2
                fresh-=1
                visited.add((x,y))
                q.append((x,y,time+1))
        
        return maxTime if fresh==0 else -1

