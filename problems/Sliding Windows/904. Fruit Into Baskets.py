class Solution(object):
    def totalFruit(self, fruits):
        windowStart = 0
        bestLength = 0
        hashmap = {}
        
        for windowEnd in range(len(fruits)):
            fruit = fruits[windowEnd]
            if fruit not in hashmap:
                hashmap[fruit] = 0
            hashmap[fruit] += 1
            
            while len(hashmap) > 2:
                startFruit = fruits[windowStart]
                hashmap[startFruit] -= 1
                if hashmap[startFruit] == 0:
                    del hashmap[startFruit]
                windowStart += 1
                
            bestLength = max(bestLength, windowEnd - windowStart + 1)
            
        return bestLength
            
            
            