class Solution(object):
    def climbStairs(self, n):
        return self.solveDP(n, {})
    
    def solveDP(self,n, memo):
        if n in memo:
            return memo[n]
        if n < 0:
            return 0
        if n == 0:
            return 1

        memo[n] = self.solveDP(n-1, memo) + self.solveDP(n-2, memo)
        
        return memo[n]