# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
from collections import deque
candidates = [2,3,6,7]
target = 7

class subArray:
    def __init__(self, array, total, index):
        self.array = array
        self.total = total
        self.index = index

subsets = deque()
result = []

for idx1 in range(len(candidates)):
    currentCandidate = candidates[idx1]
    subsets.append(
        subArray([currentCandidate], currentCandidate, idx1)
    )
    
    while subsets:
        currentSet = subsets.popleft()
        currentTotal = currentSet.total
        currentIndex = currentSet.index
        if currentTotal == target:
            result.append(currentSet.array)
        elif currentTotal < target:
            for idx2 in range(currentIndex, len(candidates)):
                copyCurrentSet = list(currentSet.array)
                copyCurrentSet.append(candidates[idx2])
                subsets.append(
                    subArray(copyCurrentSet, currentTotal + candidates[idx2], idx2)
                )
result 