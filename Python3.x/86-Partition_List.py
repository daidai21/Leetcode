# Runtime: 44 ms, faster than 45.75% of Python3 online submissions for Partition List.
# Memory Usage: 13.8 MB, less than 5.45% of Python3 online submissions for Partition List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        tmp1 = p1 = ListNode(None)
        tmp2 = p2 = ListNode(None)
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None
        p1.next = tmp2.next
        return tmp1.next
