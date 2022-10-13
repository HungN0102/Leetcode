# Write a function to find the start/ end index of an array that needs to be sorted

def subarraySort(array):
    left = 0 
    right = len(array) - 1
    isWrong = False
    while left + 1 <= len(array) - 1:
        if array[left] > array[left+1]:
            isWrong = True
            break
        left += 1

    if not isWrong:
        return [-1, -1]
        
    while right - 1 >= 0:
        if array[right] < array[right-1] or array[right] < array[left]:
            isWrong = True
            break 
        right -= 1
    
    minSub = min(array[left:right+1])
    maxSub = max(array[left:right+1])
    
    left = 0
    while minSub >= array[left]:
        left += 1
        
    right = len(array) - 1
    while maxSub <= array[right]:
        right -= 1
        
    return [left, right]