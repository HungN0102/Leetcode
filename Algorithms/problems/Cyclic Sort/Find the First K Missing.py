# Given an unsorted array containing numbers and a number ‘k’. 
# Find the first ‘k’ missing positive numbers in the array.
nums = [2, 3, 4]
k = 3

def first_k_missing(nums, k):    
    i = 0
    while i <= len(nums) - 1:
        if nums[i] >= 0 and nums[i] <= len(nums) and nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
            else: 
                i += 1
        else:
            i += 1
            
    k_missing = []
    extra_nums = set()
    for i in range(len(nums)):
        if nums[i] != i + 1:
            if len(k_missing) < k:
                k_missing.append(i+1)
                extra_nums.add(nums[i])
    
    extra_nums = list(extra_nums)
    candidate_value = len(nums) + 1
    while len(k_missing) < k:
        if candidate_value not in extra_nums:
            k_missing.append(candidate_value)
        candidate_value += 1
    
    return k_missing

first_k_missing(nums, k)