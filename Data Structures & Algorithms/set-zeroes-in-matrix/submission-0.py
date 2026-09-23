class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visited=set()
        m=len(matrix)
        n=len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    visited.add((i,j))
        
        for r,c in visited:
            for i in range(n):
                matrix[r][i]=0
            for i in range(m):
                matrix[i][c]=0