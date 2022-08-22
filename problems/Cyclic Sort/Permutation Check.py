# A non-empty array A consisting of N integers is given.

# A permutation is a sequence containing each element from 1 to N once, and only once.

def solution(A):
    i = 0
    while i <= len(A) - 1:
        if A[i] != i + 1:
            j = A[i] - 1
            if j <= len(A) - 1 and A[i] != A[j]:
                A[j], A[i] = A[i], A[j]
            else:
                i += 1
        else:
            i += 1
    
    for i in range(len(A)):
        if A[i] != i + 1:
            return 0

    return 1