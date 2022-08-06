# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

from heapq import *

class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []
        maxRooms = 0
        
        for i in range(len(intervals)):
            while len(heap) > 0 and intervals[i][0] >= heap[0]:
                heappop(heap)
            heappush(heap,intervals[i][1])
            maxRooms = max(maxRooms, len(heap))
        return maxRooms