class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        visited=set()
        fresh_count=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    visited.add((i,j))
                elif grid[i][j]==1:
                    fresh_count+=1

        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        total_time=0

        while q:
            r,c,time=q.popleft()
            total_time=max(total_time,time)
            for dr,dc in directions:
                x=dr+r
                y=dc+c
                if x<0 or x>m-1 or y<0 or y>n-1 or grid[x][y]==0 or (x,y) in visited:
                    continue
                
                grid[x][y]=2
                fresh_count-=1
                q.append((x,y,time+1))
                visited.add((x,y))
        
        return total_time if fresh_count==0 else -1
        
