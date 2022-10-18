def climbStairs(n):
    return solveDP(n, {})

def solveDP(n, memo):
    if n in memo:
        return memo[n]
    if n < 0:
        return 0
    if n == 0:
        return 1

    memo[n] = solveDP(n-1, memo) + solveDP(n-2, memo)
    
    return memo[n]

climbStairs(8)