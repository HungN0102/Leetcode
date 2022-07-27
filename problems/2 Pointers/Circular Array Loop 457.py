nums = [2, 1, -1, -2]

def move_index(index):
    N = len(nums)
    newIndex = (nums[index] + index) % N
    return newIndex

def cycle_check(nums):
    for i in range(len(nums)):
        direction = nums[i] >= 0
        slow = i 
        fast = i
        
        while True:
            slow = move_index(slow)
            
            fast = move_index(fast)
            if fast == move_index(fast):
                break
            
            fast = move_index(fast)
            
            direction_slow = nums[slow] >= 0
            direction_fast = nums[fast] >= 0
            
            if direction_fast == direction and direction_slow == direction and fast == slow:
                return True 
            
            elif direction_fast != direction or direction_slow != direction:
                break 
            
    return False 

cycle_check(nums)