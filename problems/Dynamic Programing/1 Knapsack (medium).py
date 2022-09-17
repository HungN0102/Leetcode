# Top down DP with memo

weights =[2, 3, 1, 4]
profits = [4, 5, 3, 7]
capacity = 5

def solve_knapsack(weights, profits, capacity):
    memo = [[-1 for _ in range(len(profits)+1)] for _ in range(capacity+1)]
    return recursive_knapsack(weights, profits, capacity, 0, memo)

def recursive_knapsack(weights, profits, capacity, currentIndex, memo):
    if memo[capacity][currentIndex] != -1:
        return memo[capacity][currentIndex]
    if capacity <= 0:
        return 0
    if currentIndex >= len(weights):
        return 0
    
    profit1 = 0
    if capacity >= weights[currentIndex]:
        profit1 = profits[currentIndex] + recursive_knapsack(weights, profits, capacity-weights[currentIndex], currentIndex+1, memo)
    profit2 = recursive_knapsack(weights, profits, capacity, currentIndex+1, memo)
    
    memo[capacity][currentIndex] = max(profit1, profit2)
    return memo[capacity][currentIndex]

solve_knapsack(weights, profits, capacity)


