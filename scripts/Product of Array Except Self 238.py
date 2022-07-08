def arrayOfProducts(array):
    fromLeftProducts = [1 for _ in range(len(array))]
    fromRightProducts = [1 for _ in range(len(array))]
    
    outputList = []
    product = 1
    for i in range(len(array)):
        fromLeftProducts[i] = product*array[i]
        product *= array[i]
    
    product = 1
    for i in reversed(range(len(array))):
        fromRightProducts[i] = product*array[i]
        product *= array[i]
    
    for i in range(len(array)):
        product = 1
        if i < len(array) - 1:
            product *= fromRightProducts[i+1]
        if i > 0:
            product *= fromLeftProducts[i-1]
        outputList.append(product)
    return outputList

arrayOfProducts([1,2,3,4])