class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        m=len(mat)
        n=len(mat[0])

        for i in range(m):
            for j in range(i,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        # mat.reverse()
        for i in range(len(mat)):
            mat[i].reverse()