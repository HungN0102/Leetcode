islands = [[1, 1, 1, 0, 0], 
            [0, 1, 0, 0, 1], 
            [0, 0, 1, 1, 0], 
            [0, 0, 1, 0, 0], 
            [0, 0, 1, 0, 0]]


def largest_island(islands):
    rows = len(islands)
    cols = len(islands[0])
    largestArea = 0
    
    for rIdx in range(rows):
        for cIdx in range(cols):
            if islands[rIdx][cIdx] == 1:
                largestArea = max(largestArea, area_island(islands, rIdx, cIdx))
                
    return largestArea 

def area_island(islands, rIdx, cIdx):
    if rIdx < 0 or cIdx < 0 or rIdx >= len(islands) or cIdx >= len(islands[0]):
        return 0
    if islands[rIdx][cIdx] == 0:
        return 0
    
    islands[rIdx][cIdx] = 0
    area = 1
    
    area += area_island(islands, rIdx+1, cIdx)
    area += area_island(islands, rIdx-1, cIdx)
    area += area_island(islands, rIdx, cIdx+1)
    area += area_island(islands, rIdx, cIdx-1)
    
    return area
    
    
largest_island(islands)