class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visitSet=set()
        area=0 
        def dfs(i,j):
            if (i<0 or i>rows-1 or j<0 or j>cols-1 or (i,j) in visitSet or grid[i][j]==0):
                return 0
            
            visitSet.add((i,j))
            return 1+ (dfs(i-1,j)+dfs(i+1,j)+dfs(i,j+1)+dfs(i,j-1))


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    if (i,j) not in visitSet:
                        area=max(area,dfs(i,j))

        return area