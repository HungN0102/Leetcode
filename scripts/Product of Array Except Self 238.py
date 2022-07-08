def arrayOfProducts(array):
    outputList = []
    leftArea = 1
    for i in range(len(array)):
        number = leftArea
        leftIndex = i + 1
        while leftIndex <= len(array) - 1:
            number *= array[leftIndex]
            leftIndex += 1
        
        leftArea *= array[i]
        outputList.append(number)
    return outputList
