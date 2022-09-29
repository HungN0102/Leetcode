# Input: m = 3, n = 7
# Output: 28

class Solution:
    def uniquePaths(self, rows, columns, result=0, memo={}):
        key = str(rows) + "," + str(columns)
        if key in memo:
            return memo[key]
        if rows == 1 and columns == 1:
            return 1
        if rows <= 0 or columns <= 0:
            return 0

        memo[key] = self.uniquePaths(rows-1, columns, result) + self.uniquePaths(rows, columns-1, result)

        return memo[key]