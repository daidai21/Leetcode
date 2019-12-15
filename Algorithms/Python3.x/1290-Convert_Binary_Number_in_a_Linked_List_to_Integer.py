# Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head is not None:
            result = result * 2 + head.val
            head = head.next
        return result
