from contextlib import nullcontext


numbers = [1,2,3,5,25]
target = 100

def bestSum(numbers, target, memo = {}):
    if target in memo:
        return memo[target]
    if target < 0:
        return None
    if target == 0:
        return []
    
    currentShortest = None
    for number in numbers:
        remainder = target - number
        combination = bestSum(numbers, remainder, memo)
        if combination is not None:
            currentCombination = combination + [number]
            if currentShortest is None or len(currentCombination) < len(currentShortest):
                currentShortest = currentCombination
                
    memo[target] = currentShortest
    return currentShortest

bestSum(numbers, target, {})