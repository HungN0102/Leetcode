# We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.

# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without using any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

arr = [3, 1, 5, 4, 2]

def cyclic_sort(nums):
    i = 0
    while i <= len(arr) - 2:
        if arr[i] == i + 1:
            i += 1
        else:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
    return nums 
