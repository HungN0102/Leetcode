class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        rightStart = len(cardPoints) - k
        currentSum = sum(cardPoints[rightStart:])
        maxSum = currentSum
        left = 0

        if k == len(cardPoints):
            print(sum(cardPoints))

        for right in range(rightStart, len(cardPoints)):
            currentSum -= cardPoints[right]
            currentSum += cardPoints[left]
            maxSum = max(maxSum, currentSum)
            left += 1

        return maxSum