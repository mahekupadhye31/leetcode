class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        visited=set()

        def dfs(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1 or (i,j) in visited or grid[i][j]=="0":
                return 
            visited.add((i,j))
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    if (i,j) not in visited:
                        dfs(i,j)
                        count+=1
        return count