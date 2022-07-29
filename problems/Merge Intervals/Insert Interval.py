Intervals=[[2,3],[5,7]]
newInterval=[1,4]

i = 0
outputList = []

while i <= len(Intervals) - 1:
    newStart = newInterval[0]
    while i <= len(Intervals) - 1 and Intervals[i][1] < newStart:
        outputList.append(Intervals[0])
        i += 1
        
    newEnd = newInterval[1]
    while i <= len(Intervals) - 1 and Intervals[i][0] <= newEnd:
        newStart = min(newStart, Intervals[i][0])
        newEnd = max(newEnd, Intervals[i][1])
        i += 1 
        
    outputList.append([newStart,newEnd])
    
    while i <= len(Intervals) - 1:
        outputList.append(Intervals[i])
        i += 1
        
outputList