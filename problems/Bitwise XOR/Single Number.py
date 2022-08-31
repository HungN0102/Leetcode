# In a non-empty array of integers, every number appears twice except for one, find that single number.

arr = [1, 4, 2, 1, 3, 2, 3]

def find_single(arr):
    num = 0
    for i in range(len(arr)):
        num ^= arr[i]
        
    return num 

