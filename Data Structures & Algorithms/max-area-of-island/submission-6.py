class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        maxArea=0
        visited=set()

        def dfs(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1 or (i,j) in visited or grid[i][j]==0:
                return 0
            visited.add((i,j))
            return 1+ (dfs(i-1,j)+dfs(i+1,j)+dfs(i,j+1)+dfs(i,j-1))
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    maxArea=max(maxArea,dfs(i,j))
        return maxArea