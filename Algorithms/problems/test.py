def coinChange(coins, amount):
    coins.sort()
    dp = [float("inf") for _ in range(amount+1)]
    dp[0] = 0
    
    for target in range(1, amount+1):
        for c in coins:
            if target - c >= 0:
                dp[target] = min(dp[target], dp[target-c]+1)
        
    return dp[-1]
coinChange([186,419,83,408],6249)