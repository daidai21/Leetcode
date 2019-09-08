# Runtime: 48 ms, faster than 71.28% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.8 MB, less than 5.17% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # if head is None or head.next is None:
        #     return head
        res = pre = ListNode(None)
        res.next, cur = head, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur and cur.next and cur.next.val == cur.val:
                    cur = cur.next
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return res.next
