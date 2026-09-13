class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        rotten=0
        fresh=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    rotten+=1
                    q.append((i,j,0))     #0 no of minute at which i,j is rotten
                    visited.add((i,j))
        
        time=0
        while q:
            i,j,minute=q.popleft()
            time=max(time,minute)
            directions=[[1,0],[0,1],[-1,0],[0,-1]]
            for dr,dc in directions:
                x=dr+i
                y=dc+j
                if x<0 or x>rows-1 or y<0 or y>cols-1 or (x,y) in visited or grid[x][y]==0:
                    continue
                grid[x][y]=2
                visited.add((x,y))
                q.append((x,y,minute+1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
        
        if fresh>0:
            return -1
        
        return time