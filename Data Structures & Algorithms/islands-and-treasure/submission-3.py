class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        visited=set()

        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j,0))
                    visited.add((i,j))

        directions=[[1,0],[0,1],[-1,0],[0,-1]]

        while q:
            r,c,dist=q.popleft()
            #visited.add((r,c))
            for dr,dc in directions:
                x=dr+r
                y=dc+c
                if x<0 or x>m-1 or y<0 or y>n-1 or grid[x][y]==-1 or grid[x][y]<dist+1 or (x,y) in visited:
                    continue
                
                grid[x][y]=dist+1
                q.append((x,y,grid[x][y]))
                visited.add((x,y))
                
