# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution(object):
    def exist(self, board, word):
        nrows = len(board)
        ncols = len(board[0])

        visited = [[0 for _ in range(ncols)] for _ in range(nrows)]
        for r in range(nrows):
            for c in range(ncols):
                if board[r][c] == word[0]:
                    if self.backtrack(board, word, r, c, 0, visited):
                        return True 

        return False

    def backtrack(self, board, word, r, c, i, visited):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or visited[r][c] == 1 or board[r][c] != word[i]:
            return False

        visited[r][c] = 1
        result = (
                self.backtrack(board, word, r+1, c, i+1, visited) or 
                self.backtrack(board, word, r-1, c, i+1, visited) or
                self.backtrack(board, word, r, c+1, i+1, visited) or
                self.backtrack(board, word, r, c-1, i+1, visited)
                )

        visited[r][c] = 0

        return result