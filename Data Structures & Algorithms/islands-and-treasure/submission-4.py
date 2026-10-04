class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        visited=set()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((0,i,j))
                    visited.add((i,j))

        directions=[[1,0],[0,1],[-1,0],[0,-1]]

        while q:
            dist,row,col=q.popleft()
            for dr,dc in directions:
                x=dr+row
                y=dc+col
                if x<0 or x>m-1 or y<0 or y>n-1 or grid[x][y]<dist+1 or (x,y) in visited or grid[x][y]==-1:
                    continue
                grid[x][y]=dist+1
                q.append((dist+1,x,y))
                visited.add((x,y))
