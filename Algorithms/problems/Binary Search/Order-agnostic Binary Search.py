# Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
def solution(nums, target):
    start = 0
    end = len(nums) - 1
    middle = int((end+start)/2)
    
    while nums[middle] != target:
        if start == end:
            return -1 
        
        if nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
        middle = int((end+start)/2)
    return middle


int(2.5)