islands = [[1, 1, 1, 0, 0], 
            [0, 1, 0, 0, 1], 
            [0, 0, 1, 1, 0], 
            [0, 0, 1, 0, 0], 
            [0, 0, 1, 0, 0]]

def number_islands(islands):
    rows = len(islands)
    cols = len(islands[0])
    noIslands = 0
    
    for rIdx in range(rows):
        for cIdx in range(cols):
            if islands[rIdx][cIdx] == 1:
                noIslands += 1
                visited_islands(islands, rIdx, cIdx)
    return noIslands 

def visited_islands(islands, rIdx, cIdx):
    if rIdx < 0 or cIdx < 0 or rIdx >= len(islands) or cIdx >= len(islands[0]):
        return 
    if islands[rIdx][cIdx] == 0:
        return 
    
    islands[rIdx][cIdx] = 0
    visited_islands(islands, rIdx-1, cIdx)
    visited_islands(islands, rIdx+1, cIdx)
    visited_islands(islands, rIdx, cIdx-1)
    visited_islands(islands, rIdx, cIdx+1)
    
number_islands(islands)