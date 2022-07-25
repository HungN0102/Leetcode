class Solution(object):
    def longestMountain(self, arr):
        i = 1
        longestPeak = 0
        
        while i < len(arr) - 1:
            isPeak = arr[i] > arr[i+1] and arr[i] > arr[i-1]
            if not isPeak:
                i += 1
                continue

            leftIndex = i - 2
            while leftIndex >= 0 and arr[leftIndex] < arr[leftIndex + 1]:
                leftIndex -= 1

            rightIndex = i + 2
            while rightIndex <= len(arr) - 1 and arr[rightIndex] < arr[rightIndex-1]:
                rightIndex += 1

            currentPeak = rightIndex - leftIndex - 1
            longestPeak = max(currentPeak, longestPeak)
        
            i = rightIndex
        return longestPeak
            
        