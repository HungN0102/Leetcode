# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

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