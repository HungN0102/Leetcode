from collections import deque
candidates = [2,5,2,1,2]
target = 5

class subArray:
    def __init__(self, array, total, index):
        self.array = array
        self.total = total
        self.index = index

candidates.sort()
subsets = deque()
result = []

for idx1 in range(len(candidates)):
    currentCandidate = candidates[idx1]
    if idx1 > 0 and candidates[idx1-1] == candidates[idx1]:
        continue
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
            for idx2 in range(currentIndex+1, len(candidates)):
                if idx2 > currentIndex + 1 and candidates[idx2] == candidates[idx2-1]:
                    continue
                copyCurrentSet = list(currentSet.array)
                copyCurrentSet.append(candidates[idx2])
                subsets.append(
                    subArray(copyCurrentSet, currentTotal + candidates[idx2], idx2)
                )
result 