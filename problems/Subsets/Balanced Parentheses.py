# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

class parentheses:
    def __init__(self, form, open, end):
        self.form = form
        self.open = open
        self.end = end 
        
from collections import deque
def solution(N):
    result = []
    
    subsets = deque()
    subsets.append(parentheses("",0,0))
    while subsets:
        currentParen = subsets.popleft()
        if currentParen.open == 3 and currentParen.end == 3:
            result.append(currentParen.form)
        else:
            if currentParen.open < 3:
                subsets.append(
                    parentheses(currentParen.form + "(", currentParen.open+1, currentParen.end)
                )
            if currentParen.end < currentParen.open:
                subsets.append(
                    parentheses(currentParen.form + ")", currentParen.open, currentParen.end+1)
                )
    return result 

solution(3)          