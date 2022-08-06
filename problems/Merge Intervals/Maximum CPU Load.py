from heapq import *

intervals = [[1,4,2], [2,4,1], [3,6,5]]
heap = []
maxCpu = 0
cpu = 0

intervals.sort(key=lambda x:x[0])
for i in range(len(intervals)):
    while len(heap) > 0 and intervals[i][0] >= heap[0][1]:
        cpu -= heap[0][2]
        heappop(heap)
    cpu += intervals[i][2]
    heappush(heap, intervals[i])
    maxCpu = max(maxCpu, cpu)
    
maxCpu

        