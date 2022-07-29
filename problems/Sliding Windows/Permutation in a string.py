# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
def find_permutation(string, pattern):
    hashmap = {}
    uniqueLetter = 0
    match = 0
    for p in pattern:
        if p not in hashmap:
            hashmap[p] = 0
            uniqueLetter += 1
        hashmap[p] += 1
        
    windowStart = 0
    for windowEnd in range(len(string)):
        rightChar = string[windowEnd]
        if rightChar in hashmap:
            hashmap[rightChar] -= 1
            if hashmap[rightChar] == 0:
                match += 1
        
        if windowEnd > len(pattern) -1:
            leftChar = string[windowStart]
            if leftChar in hashmap:
                if hashmap[leftChar] == 0:
                    match -= 1
                    hashmap[leftChar] += 1
            windowStart += 1
            
        if match == uniqueLetter:
            return True 

    return False