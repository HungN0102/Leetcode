class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        count = 0
        A.sort()
        for i in range(len(A)-2):
            targetSum = target - A[i]
            left = i + 1
            right = len(A) - 1

            while left < right:
                currentSum = A[left] + A[right]
                if currentSum > targetSum:
                    right -= 1
                elif currentSum < targetSum:
                    left += 1
                elif currentSum == targetSum and A[left] != A[right]:
                    leftCount = 1
                    rightCount = 1
                    while A[left+1] == A[left] and left + 1 < right:
                        leftCount += 1
                        left += 1
                    while A[right-1] == A[right] and left < right - 1:
                        rightCount += 1
                        right -= 1
                    left += 1
                    right -= 1
                    count += leftCount * rightCount 
                elif currentSum == targetSum and A[left] == A[right]:
                    lengthSub = right - left + 1
                    count += lengthSub * (lengthSub-1)/2
                    break
        return int(count % MOD)