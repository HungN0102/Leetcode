# You are given a 2D matrix containing only 1s (land) and 0s (water).
# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). 
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).
# There are no lakes on the island, so the water inside the island is not connected to the water around it. A cell is a square with a side length of 1.. 
# The given matrix has only one island, write a function to find the perimeter of that island.

islands =  [[1, 1, 0, 0, 0], 
            [0, 1, 0, 0, 0], 
            [0, 1, 0, 0, 0], 
            [0, 1, 1, 0, 0], 
            [0, 0, 0, 0, 0]]

def island_perimeter(islands):
    rows = len(islands)
    cols = len(islands[0])
    visited = [[False for i in range(rows)] for j in range(cols)]
   
    for rIdx in range(rows):
        for cIdx in range(cols):
            if islands[rIdx][cIdx] == 1 and visited[rIdx][cIdx] == False:
                perimeter = perimeter_count(islands, rIdx, cIdx, visited)
                
    return perimeter
                
def perimeter_count(islands, rIdx, cIdx, visited):
    if rIdx < 0 or cIdx < 0 or rIdx >= len(islands) or cIdx >= len(islands[0]):
        return 1
    elif islands[rIdx][cIdx] == 0 and not visited[rIdx][cIdx]:
        return 1
    elif visited[rIdx][cIdx]:
        return 0
    visited[rIdx][cIdx] = True 
    perimeter = 0
    
    perimeter += perimeter_count(islands, rIdx+1, cIdx, visited)
    perimeter += perimeter_count(islands, rIdx-1, cIdx, visited)
    perimeter += perimeter_count(islands, rIdx, cIdx+1, visited)
    perimeter += perimeter_count(islands, rIdx, cIdx-1, visited)
    
    return perimeter
    
island_perimeter(islands)