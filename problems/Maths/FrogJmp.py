# A small frog wants to get to the other side of the road. 
# The frog is currently located at position X and wants to get to a position greater than or equal to Y. 
# The small frog always jumps a fixed distance, D.

import math
def solution(X, Y, D):
    distance = Y - X 
    jump = math.ceil(distance / D)
    return jump


solution(10,85,30)