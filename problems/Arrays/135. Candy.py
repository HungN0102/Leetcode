# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

array = [8, 4, 2, 1, 3, 6, 7, 9, 5]

def min_rewards(array):
    awards = [1 for _ in range(len(array))]
    
    for i in range(1,len(array)):
        if array[i] == array[i-1]:
            awards[i] = awards[i-1]
        elif array[i] > array[i-1]:
            awards[i] = awards[i-1] + 1
    
    for i in range(len(array)-2,-1,-1):
        if awards[i] <= awards[i+1]:
            if array[i] > array[i+1]:
                awards[i] = awards[i+1] + 1
        
    return sum(awards)

min_rewards(array)