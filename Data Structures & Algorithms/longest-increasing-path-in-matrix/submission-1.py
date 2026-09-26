class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        distances=[[-1]*n for i in range(m)]
        maxLen=float("-inf")

        def dfs(i,j,prev):
            nonlocal maxLen

            if i<0 or i>m-1 or j<0 or j>n-1 or matrix[i][j]<=prev:
                return 0

            if distances[i][j]!=-1:
                return distances[i][j]

            distances[i][j]=1+ max(dfs(i-1,j,matrix[i][j]),
            dfs(i+1,j,matrix[i][j]), dfs(i,j+1,matrix[i][j]), dfs(i,j-1,matrix[i][j])) 

            maxLen=max(maxLen,distances[i][j])

            return distances[i][j]

        
        for i in range(m):
            for j in range(n):
                dfs(i,j,float("-inf"))
        return maxLen
