# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, k):
        dummy = ListNode(0)
        origin = dummy
        dummy.next = head

        length = 0
        while dummy.next:
            dummy = dummy.next
            length += 1

        dummy = origin
        i = 0
        while i < length - k:
            dummy = dummy.next
            i += 1
        dummy.next = dummy.next.next

        return origin.next
        