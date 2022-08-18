# Given a set of distinct numbers, find all of its permutations.
# Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:
from collections import deque
nums = [1,3,5]

numsLength = len(nums)
result = []
permutations = deque()
permutations.append([])
for currentNumber in nums:
    # we will take all existing permutations and add the current number to create 
    # new permutations
    n = len(permutations)
    for _ in range(n):
        oldPermutation = permutations.popleft()
        # create a new permutation by adding the current number at every position
        for j in range(len(oldPermutation)+1):
            newPermutation = list(oldPermutation)
            newPermutation.insert(j, currentNumber)
            if len(newPermutation) == numsLength:
                result.append(newPermutation)
            else:
                permutations.append(newPermutation)