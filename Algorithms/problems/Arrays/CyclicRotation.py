# An array A consisting of N integers is given. 
# Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. 
# For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

def solution(A, k):
    outputList = [0 for _ in range(len(A))]
    
    for i in range(len(A)):
        newIndex = (i + k) % len(A)
        outputList[newIndex] = A[i]
        
    return outputList 

solution([3, 8, 9, 7, 6], 6)
