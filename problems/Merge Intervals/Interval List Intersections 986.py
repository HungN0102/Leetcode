class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        firstIndex = 0
        secondIndex = 0
        outputList = []
        
        while firstIndex < len(firstList) and secondIndex < len(secondList):
            firstStart = firstList[firstIndex][0]
            firstEnd = firstList[firstIndex][1]
            
            secondStart = secondList[secondIndex][0]
            secondEnd = secondList[secondIndex][1]
            
            firstInSecond = firstStart >= secondStart and firstStart <= secondEnd
            secondInFirst = secondStart >= firstStart and secondStart <= firstEnd 
            
            if firstInSecond or secondInFirst:
                outputList.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])
                
            if firstEnd < secondEnd:
                firstIndex += 1
            else:
                secondIndex += 1
                
        return outputList