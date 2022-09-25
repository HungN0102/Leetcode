def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                isSorted = False
                array[i+1], array[i] = array[i], array[i+1]
        counter += 1
    return array

