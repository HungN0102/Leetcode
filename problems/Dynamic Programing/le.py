# Given the weights and profits of ‘N’ items, 
# we are asked to put these items in a knapsack with a capacity ‘C.’ 

# The goal is to get the maximum profit out of the knapsack items. 
# Each item can only be selected once, 
# as we don’t have multiple quantities of any item.

nums = [3, 0, 1, 2]

def solve_knapsack(nums):
    s = sum(nums)
    sHalf = s/2
    if s % 2 != 0:
        return False
    
    return knapsack_recursive(nums, s, sHalf, 0)

def knapsack_recursive(nums, total, target, currentIndex):
    if currentIndex >= len(nums):
        return False 
    if total == target:
        return True
    
    isEqual = False 
    
    isEqual |= knapsack_recursive(nums, total-nums[currentIndex], target, currentIndex+1)
    isEqual |= knapsack_recursive(nums, total, target, currentIndex+1)
    
    return isEqual

solve_knapsack(nums)