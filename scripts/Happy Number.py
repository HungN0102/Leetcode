# Any number will be called a happy number if, after repeatedly replacing it with 
# a number equal to the sum of the square of all of its digits, leads us to number ‘1’. 
# All other (not-happy) numbers will never reach ‘1’. 
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

num = 23 

def find_square_sum(num):
    sum_ = 0
    while num > 0:
        digit = num % 10
        sum_ += digit*digit 
        num //= 10
    return sum_
    
def isHappy(num):
    slow = num
    fast = num 
    while True:
        slow = find_square_sum(slow)
        
        fast = find_square_sum(fast)
        fast = find_square_sum(fast)
        if slow == fast:
            break
        
    outcome = (slow == 1)
    return  outcome

isHappy(num)