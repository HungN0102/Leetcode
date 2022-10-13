def diskStacking(disks):
    stacks = [[] for _ in range(len(disks))]
    maxHeights = [0 for _ in range(len(disks))]
    
    stacks[0] = disks[0]
    maxHeights[0] = disks[0][-1]
    for currentIndex in range(len(disks)):
        for secondIndex in range(0, currentIndex):
            if checkStack(disks[currentIndex], disks[secondIndex]) and maxHeights[currentIndex] > disks[secondIndex][-1] + disks[currentIndex][-1]:
                stacks[currentIndex] = stacks[secondIndex] + disks[currentIndex]
                maxHeights[currentIndex] = disks[secondIndex][-1] + disks[currentIndex][-1]
    return maxHeights

def checkStack(biggerDisk, smallerDisk):
    for i in range(3):
        if smallerDisk[i] > biggerDisk[i]:
            return False 
    return True


disks = [
    [2, 1, 2],
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [1, 3, 1],
    [4, 4, 5]
  ]

diskStacking(disks)