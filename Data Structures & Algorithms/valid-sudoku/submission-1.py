class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m=len(board)
        n=len(board[0])
        rows=defaultdict(set)
        cols=defaultdict(set)
        squares=defaultdict(set)

        for i in range(m):
            for j in range(n):
                if board[i][j]==".":
                    continue
                if (board[i][j] in squares[(i//3,j//3)]) or (board[i][j] in rows[i]) or (board[i][j] in cols[j]):
                    return False
                squares[(i//3,j//3)].add(board[i][j])
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
        return True