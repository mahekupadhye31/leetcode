class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        pacific=set()
        atlantic=set()

        def dfs(i,j,visited,prevHeight):
            if i<0 or i>m-1 or j<0 or j>n-1 or heights[i][j]<prevHeight or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i-1,j,visited,heights[i][j])
            dfs(i+1,j,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])
            dfs(i,j+1,visited,heights[i][j])
            return

        for i in range(m):
            dfs(i,0,pacific,-1)

        for i in range(m):
            dfs(i,n-1,atlantic,-1)

        for i in range(n):
            dfs(0,i,pacific,-1)

        for i in range(n):
            dfs(m-1,i,atlantic,-1)

        result=[]

        for elem in pacific:
            if elem in atlantic:
                result.append(elem)
        return result
        