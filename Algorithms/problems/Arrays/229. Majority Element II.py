# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

array = [3,2,3]

def findElements(array):
    hashmap = {}
    validElements = []
    
    for number in array:
        if number not in hashmap:
            hashmap[number] = 0
        hashmap[number] += 1
        
    threshold = len(array)/3
    for k, v in hashmap.items():
        if v > threshold:
            validElements.append(k)
    
    return validElements

findElements(array)