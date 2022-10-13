def sunsetViews(buildings, direction):
    stepIndex = 1 if direction == 'WEST' else -1
    currentIndex = 0 if direction == 'WEST' else len(buildings) - 1
    maxHeight = 0

    outputList = []
    while currentIndex >= 0 and currentIndex <= len(buildings) - 1:
        currentHeight = buildings[currentIndex]
        if currentHeight > maxHeight:
            outputList.append(currentIndex)
        currentIndex += stepIndex
        maxHeight = max(maxHeight, currentHeight)

    if direction != 'WEST':
        outputList = outputList[::-1]
    return outputList
