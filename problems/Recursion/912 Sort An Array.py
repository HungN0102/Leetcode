class Solution(object):
    def sortArray(self, nums):
        if len(nums) < 2:
            return nums
        
        midpoint = len(nums) // 2
        sortedFirstHalf = self.sortArray(nums[:midpoint])
        sortedSecondHalf = self.sortArray(nums[midpoint:])
        return self.sortTwoArrays(sortedFirstHalf, sortedSecondHalf)
        
    def sortTwoArrays(self, list1, list2):
        index1 = 0
        index2 = 0
        mergedList = []
        
        while index1 <= len(list1) - 1 and index2 <= len(list2) - 1:
            if list1[index1] < list2[index2]:
                mergedList.append(list1[index1])
                index1 += 1
            else:
                mergedList.append(list2[index2])
                index2 += 1
        mergedList += list1[index1:]
        mergedList += list2[index2:]
        return mergedList
    