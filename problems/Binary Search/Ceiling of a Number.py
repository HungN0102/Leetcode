# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

nums = [1, 3, 8, 10, 15]
key = 7

def solution(nums, key):
    start = 0
    end = len(nums) - 1
    
    if key > nums[end]:
        return -1
    
    while start <= end:
        mid = int((end+start)/2)
        if nums[mid] > key:
            end = mid - 1
        elif nums[mid] < key:
            start = mid + 1
        else:
            return mid 
        
    return start 

solution(nums, key)