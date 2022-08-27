# Any image can be represented by a 2D integer array (i.e., a matrix) where each cell represents the pixel value of the image.

# Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The given color is applied to all horizontally and vertically connected cells with the same color as that of the starting cell. Recursively, the algorithm fills cells with the new color until it encounters a cell with a different color than the starting cell. 

# Given a matrix, a starting cell, and a color, flood fill the matrix.
a = 2
islands = [[1, 1, 1, 0, 0], 
            [0, 1, 0, 0, 1], 
            [0, 0, 1, 1, 0], 
            [0, 0, 1, 0, 0], 
            [0, 0, 1, 0, 0]]

def fillDFS(islands, color, rIdx, cIdx):
    if rIdx < 0 or cIdx < 0 or rIdx >= len(islands) or cIdx >= len(islands[0]):
        return 
    if islands[rIdx][cIdx] != 1:
        return 
    a = 1
    islands[rIdx][cIdx] = color 
    
    fillDFS(islands, color, rIdx+1, cIdx)
    fillDFS(islands, color, rIdx-1, cIdx)
    fillDFS(islands, color, rIdx, cIdx+1)
    fillDFS(islands, color, rIdx, cIdx-1)
    return rIdx
    
fillDFS(islands, 5, 2, 2)
