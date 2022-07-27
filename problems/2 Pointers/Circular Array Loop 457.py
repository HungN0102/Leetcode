#You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

# If nums[i] is positive, move nums[i] steps forward, and
# If nums[i] is negative, move nums[i] steps backward.
# Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

# A cycle in the array consists of a sequence of indices seq of length k where:

# Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# Every nums[seq[j]] is either all positive or all negative.
# k > 1
# Return true if there is a cycle in nums, or false otherwise.


class Solution(object):
    def circularArrayLoop(self, nums):
        def move_index(index):
            N = len(nums)
            newIndex = (nums[index] + index) % N
            return newIndex

        for i in range(len(nums)):
            direction = nums[i] >= 0
            slow = i 
            fast = i

            while True:
                slow = move_index(slow)
                direction_slow = nums[slow] >= 0
                if direction_slow != direction:
                    break
                
                fast = move_index(fast)
                direction_fast = nums[fast] >= 0
                if fast == move_index(fast) or direction_fast != direction:
                    break

                fast = move_index(fast)
                direction_fast = nums[fast] >= 0

                if direction_fast == direction and direction_slow == direction and fast == slow:
                    return True 

                elif direction_fast != direction or direction_slow != direction:
                    break 

        return False 
        