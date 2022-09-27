candidates = [2,3,6,7]
target = 7

def combinationSum(candidates, target):
    results = []
    
    def backtrack(result=[], sumTarget=target, currentIndex=0):
        if sumTarget == 0:
            results.append(list(result))
            return 
        if sumTarget < 0:
            return
        if currentIndex >= len(candidates):
            return
        
        for i in range(currentIndex,len(candidates)):
            c = candidates[i]
            remainder = sumTarget - c
            result.append(c)
            backtrack(result, remainder, i)
            result.pop()
            
    backtrack()
    
    return results 

combinationSum(candidates, target)