intervals = [[6,7], [2,4], [5,9]]

def merge_intervals(intervals):
    intervals.sort(key = lambda x: x[0])
    i = 0
    outputList = []

    while i < len(intervals):
        preStart = intervals[i][0]
        preEnd = intervals[i][1]
        
        while i + 1 < len(intervals) and intervals[i+1][0] <= preEnd:
            preEnd = max(intervals[i+1][1], preEnd)
            i += 1
            
        outputList.append([preStart, preEnd])
        
        i += 1
    
    return outputList