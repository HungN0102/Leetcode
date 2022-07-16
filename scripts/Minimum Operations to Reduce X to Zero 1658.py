nums = [5,2,3,1,1]
nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
x = 134365
def minOperations(nums, x):
    minimum = float("inf")
    currentSum = sum(nums)
    N = len(nums)
    operations = N
    left = 0

    if currentSum < x:
        return -1
    elif currentSum == x:
        return minimum

    for right in range(N):
        currentSum -= nums[right]
        operations -= 1
        

        while currentSum < x:
            currentSum += nums[left]
            operations += 1
            left += 1
            
        if currentSum == x:
            minimum = min(operations, minimum)
            
    if minimum == float("inf"):
        return -1
    else:
        return minimum
    
    
minOperations(nums, x)