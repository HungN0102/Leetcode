# A non-empty array A consisting of N integers is given. 
# The array contains an odd number of elements, 
# and each element of the array can be paired with another element that has the same value, 
# except for one element that is left unpaired.

def solution(A):
    A.sort()
    for i in range(0,len(A),2):
        if i != len(A) - 1:
            if A[i] != A[i+1]:
                return A[i]
        else:
            return A[i]        
solution([1,1,3,3,5])
