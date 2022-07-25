class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        count = 0
        left = 0
        right = len(people) - 1
        people.sort()

        while left < right:
            currentWeight = people[left] + people[right]
            if currentWeight > limit:
                count += 1
                right -= 1
            else:
                count += 1
                right -= 1
                left += 1

        if left == right:
            count += 1
            
        return count