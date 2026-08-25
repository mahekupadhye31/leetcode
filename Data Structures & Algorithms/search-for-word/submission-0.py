class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        def search(r:int,c:int,index:int):
            if r<0 or c<0 or r>(len(board)-1) or c>(len(board[0])-1) or board[r][c]!=word[index] or (r,c) in visited:
                return False    
            if index==len(word)-1:
                return True
            visited.add((r,c)) 
            res= (search (r-1,c,index+1) or search (r+1,c,index+1) or search(r,c+1,index+1) or search(r,c-1,index+1))
            visited.remove((r,c))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and search(i,j,0):
                    return True
        return False
        