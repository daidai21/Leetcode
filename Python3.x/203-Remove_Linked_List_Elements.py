# Runtime: 76 ms, faster than 64.08% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 16.9 MB, less than 5.55% of Python3 online submissions for Remove Linked List Elements.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = ListNode(None)
        result.next = head
        p1 = result
        p2 = head
        while p2:
            if p2.val == val:
                p1.next = p2.next
            else:
                p1 = p1.next
            p2 = p2.next            
        return result.next
