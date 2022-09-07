def fourNumberSum(array, targetSum):
    array.sort()
    outputList = []
    for i in range(len(array)-3):
        for j in range(i+1, len(array)-2):
            target = targetSum - array[i] - array[j]

            left = j + 1
            right = len(array) - 1
            while left < right:
                currentSum = array[left] + array[right]
                if currentSum > target:
                    right -= 1
                elif currentSum < target:
                    left += 1
                elif currentSum == target:
                    list_ = [array[i], array[j], array[left], array[right]]
                    outputList.append(list_)
                    left += 1
                    
    return outputList