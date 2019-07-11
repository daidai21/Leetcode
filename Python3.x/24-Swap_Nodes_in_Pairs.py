# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = ListNode(None), head
        res = pre
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return res.next
