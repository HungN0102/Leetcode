islands =  [[0, 1, 1, 0, 1], 
            [0, 1, 0, 0, 1], 
            [0, 0, 1, 1, 0], 
            [0, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0]]

def number_closed_islands(islands):
    rows = len(islands)
    cols = len(islands[0])
    visited = [[False for i in range(rows)] for j in range(cols)]
    no_closed_islands = 0
    
    for rIdx in range(rows):
        for cIdx in range(cols):
            if islands[rIdx][cIdx] == 1 and visited[rIdx][cIdx] == False:
                if number_closed_islands_dfs(islands, rIdx, cIdx, visited):
                    no_closed_islands += 1
                
    return no_closed_islands

def number_closed_islands_dfs(islands, rIdx, cIdx, visited):
    if rIdx < 0 or cIdx < 0 or rIdx >= len(islands) or cIdx >= len(islands[0]):
        return False 
    if islands[rIdx][cIdx] == 0 or visited[rIdx][cIdx]:
        return True 
    
    visited[rIdx][cIdx] = True
    closed_island = True 
    
    closed_island &= number_closed_islands_dfs(islands, rIdx+1, cIdx, visited)
    closed_island &= number_closed_islands_dfs(islands, rIdx-1, cIdx, visited)
    closed_island &= number_closed_islands_dfs(islands, rIdx, cIdx+1, visited)
    closed_island &= number_closed_islands_dfs(islands, rIdx, cIdx-1, visited)
    
    return closed_island


number_closed_islands(islands)