#Given an array of points in a 2D2D plane, find ‘K’ closest points to the origin.
points = [[1, 3], [3, 4], [2, -1]]
k = 2

from heapq import *
from math import sqrt
def solution(points, k):
    maxHeap = []
    for i in range(k):
        point = points[i]
        eucDistance = sqrt(point[0]**2 + point[1]**2)
        heappush(maxHeap, [-eucDistance,point])
        
    for i in range(k, len(points)):
        point = points[i]
        eucDistance = sqrt(point[0]**2 + point[1]**2)
        if eucDistance < -maxHeap[0][0]:
            heappop(maxHeap)
            heappush(maxHeap, [-eucDistance, point])
            
    return [element[1] for element in maxHeap]

solution(points, k)