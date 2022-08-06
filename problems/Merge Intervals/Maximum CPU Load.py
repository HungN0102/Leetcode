# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

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

        