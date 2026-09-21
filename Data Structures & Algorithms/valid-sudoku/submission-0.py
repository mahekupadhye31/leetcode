class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap=defaultdict(set)
        colmap=defaultdict(set)
        squaremap=defaultdict(set)
        m=len(board)
        n=len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j]==".":
                    continue
                if board[i][j] in rowmap[i] or board[i][j] in colmap[j] or board[i][j] in squaremap[(i//3,j//3)]:
                    return False
                
                rowmap[i].add(board[i][j])
                colmap[j].add(board[i][j])
                squaremap[(i//3,j//3)].add(board[i][j])
        
        return True