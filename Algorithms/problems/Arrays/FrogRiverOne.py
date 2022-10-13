def solution(X, A):
    match = 0

    hashmap = {}
    for i in range(X):
        hashmap[i+1] = 1
    
    for i in range(len(A)):
        if A[i] in hashmap:
            if hashmap[A[i]] == 1:
                match += 1
                hashmap[A[i]] -= 1
            
        if match == X:
            return i
    return -1

solution(5,[1,3,1,4,2,3,5,4])