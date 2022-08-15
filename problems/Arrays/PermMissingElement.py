# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    i = 0
    if len(A) == 0:
        return 1

    while i <= len(A) - 1:
        if A[i] != i + 1:
            j = A[i] - 1
            if j <= len(A) - 1:
                A[j], A[i] = A[i], A[j]
            else:
                i += 1
        else:
            i += 1

    for i in range(len(A)):
        if A[i] != i+1:
            return i + 1
        
    return len(A)+1

solution([1,2,3,4,5,6,7])