# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

class Solution(object):
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        
        for rIdx in range(rows):
            for cIdx in range(cols):
                if board[rIdx][cIdx] == "O" and not visited[rIdx][cIdx]:
                    if self.isSurrounded(board, rIdx, cIdx, visited):
                        self.swapXO(board, rIdx, cIdx)
                    
    def isSurrounded(self, board, r, c, visited):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return False
        if board[r][c] == "X" or visited[r][c]:
            return True 
        
        visited[r][c] = True
        surrounded = True
        
        surrounded &= self.isSurrounded(board, r+1, c, visited)
        surrounded &= self.isSurrounded(board, r-1, c, visited)
        surrounded &= self.isSurrounded(board, r, c+1, visited)
        surrounded &= self.isSurrounded(board, r, c-1, visited)
        
        return surrounded
    
    def swapXO(self, board, r, c):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return 
        if board[r][c] == "X":
            return  
        
        board[r][c] = "X"
        
        self.swapXO(board, r+1, c)
        self.swapXO(board, r-1, c)
        self.swapXO(board, r, c-1)
        self.swapXO(board, r, c+1)
        