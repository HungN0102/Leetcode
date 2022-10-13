array = [1,2,7,1,5]
target = 9

def DP(array, target):
    results = [[0 for _ in range(target+1)] for _ in range(len(array))]
    
    for index in range(len(array)):
        results[index][0] = 1
        
    for t in range(target+1):
        results[0][t] = 0
        if t == array[0] or t == 0:
            results[0][t] = 1
            
    for index in range(len(array)):
        for t in range(target+1):
            results[index][t] = results[index-1][t] + results[index-1][t-array[index]]
    return results[-1][-1]
DP(array, target)