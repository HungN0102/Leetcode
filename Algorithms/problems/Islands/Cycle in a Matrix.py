# You are given a 2D matrix containing different characters, 
# you need to find if there exists any cycle consisting of the same character in the matrix.

# A cycle is a path in the matrix that starts and ends at the same cell and has four  or more cells. 
# From a given cell, you can move to one of the cells adjacent to it - in one of the four directions 
# (up, down, left, or right), if it has the same character value of the current cell. 

# Write a function to find if the matrix has a cycle.

board = [[1, 1, 1, 1], 
         [0, 1, 2, 1], 
         [0, 1, 2, 1], 
         [0, 1, 1, 1]]
def isCircle(board):
    rows = len(board)
    cols = len(board[0])
    visited = [[False for i in range(rows)] for j in range(cols)]
    hasCircle = False
    
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                hasCircle = isCircleDFS(board, visited, board[r][c], r, c, -1, -1)
                if hasCircle:
                    return True 
    return False

def isCircleDFS(board, visited, startChar, r, c, rOld, cOld):
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
        return False
    if board[r][c] != startChar:
        return False 
    if visited[r][c]:
        return True 
    
    visited[r][c] = True
    hasCircle = False

    hasCircle |= (r+1 != rOld and isCircleDFS(board, visited, startChar, r+1, c, r, c))
    hasCircle |= (r-1 != rOld and isCircleDFS(board, visited, startChar, r-1, c, r, c))
    hasCircle |= (c+1 != cOld and isCircleDFS(board, visited, startChar, r, c+1, r, c))
    hasCircle |= (c-1 != cOld and isCircleDFS(board, visited, startChar, r, c-1, r, c))

    return hasCircle
isCircle(board)