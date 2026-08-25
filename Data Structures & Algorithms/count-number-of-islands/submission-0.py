class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        counter=0
        visitSet=set()
        def dfs(i:int, j:int):
            if i<0 or i>rows-1 or j<0 or j>cols-1:
                return 
            if (i,j) in visitSet:
                return 
            if grid[i][j]=="0":
                return 
            visitSet.add((i,j))
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    if (i,j) not in visitSet:
                        dfs(i,j)
                        counter+=1  
        return counter

