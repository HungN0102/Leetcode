def maxSubsetSumNoAdjacent(array):
    return solve_knapsack(array, 0)

def solve_knapsack(array, currentIndex):
    if currentIndex >= len(array):
        return 0

    sum1 = array[currentIndex] + solve_knapsack(array, currentIndex+2)
    sum2 = solve_knapsack(array, currentIndex+1)

    return max(sum1, sum2)
