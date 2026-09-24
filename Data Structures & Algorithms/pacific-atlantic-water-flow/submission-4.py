class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        atlantic=set()
        pacific=set()

        def dfs(i,j,visited,prevHeight):
            if i<0 or i>m-1 or j<0 or j>n-1 or grid[i][j]<prevHeight or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i+1,j,visited,grid[i][j])
            dfs(i-1,j,visited,grid[i][j])
            dfs(i,j+1,visited,grid[i][j])
            dfs(i,j-1,visited,grid[i][j])
            return

        for i in range(m):
            dfs(i,0,pacific,grid[i][0])
        
        for i in range(m):
            dfs(i,n-1,atlantic,grid[i][n-1])
        
        for i in range(n):
            dfs(0,i,pacific,grid[0][i])
        
        for i in range(n):
            dfs(m-1,i,atlantic,grid[m-1][i])
        result=[]
        for cell in pacific:
            if cell in atlantic:
                result.append(cell)
        return result