# Runtime: 80 ms, faster than 76.84% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 14.1 MB, less than 6.25% of Python3 online submissions for Add Two Numbers II.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1, x2 = 0, 0
        while l1:
            x1 = x1 * 10 + l1.val
            l1 = l1.next
        while l2:
            x2 = x2 * 10 + l2.val
            l2 = l2.next
        x = x1 + x2
        head = ListNode(0)
        if x == 0:
            return head
        while x:
            v, x = x % 10, x // 10
            head.next, head.next.next = ListNode(v), head.next
        return head.next
