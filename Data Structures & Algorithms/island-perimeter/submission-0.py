class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()

        def dfs(i,j):
            # This side touches the grid boundary
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            # This side touches water
            if grid[i][j] == 0:
                return 1

            # Already counted this land cell
            if (i, j) in visited:
                return 0
            
            visited.add((i,j))
            return dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if (i,j) not in visited:
                        return dfs(i,j)
        return 0