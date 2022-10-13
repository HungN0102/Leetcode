intervals = [[4,5], [2,3], [3,6]]

def conflicting(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False 
    return True 

conflicting(intervals)