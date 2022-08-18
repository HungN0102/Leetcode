# Given a string, find all of its permutations preserving the character sequence but changing case.
string = "ab7c"
def solution(string):
    subsets = [string]
    for idx1 in range(len(string)):
        if string[idx1].isalpha():
            for idx2 in range(len(subsets)):
                currentStringSep = list(subsets[idx2])
                currentStringSep[idx1] = currentStringSep[idx1].swapcase()
                subsets.append("".join(currentStringSep))
                
    return subsets 

solution(string)