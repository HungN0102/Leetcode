class Solution(object):
    def findSubstring(self,s, words):
        lengthWord = len(words[0])
        n = len(words)
        startIndex = 0
        result = []
        while startIndex <= len(s) - lengthWord*n:
            currentWord = s[startIndex: startIndex+lengthWord]

            if currentWord in words:
                if self.isSubstring(s, words, startIndex) is not None:
                    result += [self.isSubstring(s, words, startIndex)]
            startIndex += 1
        return result 


    def isSubstring(self,s, words,startIndex):
        lengthWord = len(words[0])
        n = len(words)

        hashmap = {}
        for word in words:
            if word not in hashmap:
                hashmap[word] = 0
            hashmap[word] += 1

        for index in range(startIndex,startIndex+n*lengthWord, lengthWord):
            checkWord = s[index:index+lengthWord]
            if checkWord in hashmap:
                hashmap[checkWord] -= 1
                if hashmap[checkWord] == 0:
                    del hashmap[checkWord]
            else:
                return None

        if len(hashmap) == 0:
            return startIndex
        
        
            
        