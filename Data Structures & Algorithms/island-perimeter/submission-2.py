class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        m=len(grid)
        n=len(grid[0])
        def dfs(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1 or grid[i][j]==0:
                return 1

            if (i,j) in visited:
                return 0

            visited.add((i,j))
            return dfs(i,j-1) + dfs(i,j+1) + dfs(i-1,j) + dfs(i+1,j)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    perimeter=dfs(i,j) #as only one island is there
        return perimeter