# Runtime: 44 ms, faster than 99.67% of Python online submissions for Linked List Cycle II.
# Memory Usage: 17.1 MB, less than 100.00% of Python online submissions for Linked List Cycle II.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None
        while head != slow:
            head, slow = head.next, slow.next
        return head
