# Runtime: 100 ms, faster than 54.50% of Python3 online submissions for Reorder List.
# Memory Usage: 22.3 MB, less than 7.69% of Python3 online submissions for Reorder List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # find middle
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse list
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next
        # merge list
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
