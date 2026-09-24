class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()

        def dfs(r,c):
            if r<0 or r>m-1 or c<0 or c>n-1:
                return 1

            if grid[r][c]==0:
                return 1

            if (r,c) in visited:
                return 0

            visited.add((r,c))
        
            return (dfs(r+1,c) + dfs(r-1,c)+ dfs(r,c+1) + dfs(r,c-1))
        
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]==1:
                    return dfs(i,j)

        return 0