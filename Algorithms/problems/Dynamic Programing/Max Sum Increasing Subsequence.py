def maxSumIncreasingSubsequence(array):
    results = [[0, []] for _ in range(len(array))]
    results[0] = [array[0], [array[0]]]
    
    for index in range(1, len(array)):
        maxTotal = array[index]
        list_ = [array[index]]

        for reverseIndex in range(index-1, -1, -1):
            lastMaxTotal = results[reverseIndex][0]
            if maxTotal < lastMaxTotal + array[index] and array[index] > array[reverseIndex]:
                maxTotal = lastMaxTotal + array[index]
                list_ = results[reverseIndex][1] + [array[index]]
                
        results[index][0] = maxTotal
        results[index][1] = list_
    return max(results)