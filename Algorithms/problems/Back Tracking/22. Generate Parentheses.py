# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution(object):
    def generateParenthesis(self, n):
        results = []
        def backtrack(result=[], openCount=0, closeCount=0):
            if len(result) == n * 2:
                result = "".join(result)
                results.append(result)
                return
            
            if openCount < n:
                result.append("(")
                backtrack(result, openCount+1, closeCount)
                result.pop()
            if closeCount < openCount:
                result.append(")")
                backtrack(result, openCount, closeCount+1)
                result.pop()
                
        backtrack()
        
        return results
        