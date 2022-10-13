def subsets(array):
    combinations = []
    def backtrack(currentIndex, result):
        if result not in combinations:
            toAppend = list(result)
            combinations.append(toAppend)
        if currentIndex >= len(array):
            return
        
        for i in range(currentIndex, len(array)):
            number = array[i]
            result.append(number)
            backtrack(i+1, result)
            result.pop()
    backtrack(0, [])
    return combinations

subsets([1,2,3])