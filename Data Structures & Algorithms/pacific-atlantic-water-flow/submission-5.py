class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=set()
        atlantic=set()
        m=len(heights)
        n=len(heights[0])
        result=[]

        def dfs(i,j,visited,prevHeight):
            if i<0 or i>m-1 or j<0 or j>n-1 or (i,j) in visited or heights[i][j]<prevHeight:
                return
            visited.add((i,j))
            dfs(i+1,j,visited,heights[i][j])
            dfs(i-1,j,visited,heights[i][j])
            dfs(i,j+1,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])
            return

        for i in range(m):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,n-1,atlantic,heights[i][n-1])
        
        for j in range(n):
            dfs(0,j,pacific,heights[0][j])
            dfs(m-1,j,atlantic,heights[m-1][j])
        
        for pair in atlantic:
            if pair in pacific:
                result.append(pair)
        
        return [list(p) for p in result]

        
