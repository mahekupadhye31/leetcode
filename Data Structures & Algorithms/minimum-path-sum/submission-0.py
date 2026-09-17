class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for i in range(m)]

        row_total,col_total=0,0
        for i in range(m):
            row_total+=grid[i][0]
            dp[i][0]=row_total
        
        for j in range(n):
            col_total+=grid[0][j]
            dp[0][j]=col_total
        
        for i in range(1,m):
            for j in range(1,n):
                top=dp[i-1][j]
                left=dp[i][j-1]
                dp[i][j]=grid[i][j]+min(top,left)
        return dp[m-1][n-1]