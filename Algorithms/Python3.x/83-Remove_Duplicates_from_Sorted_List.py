# Runtime: 44 ms, faster than 86.52% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13 MB, less than 92.03% of Python3 online submissions for Remove Duplicates from Sorted List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur is not None and cur.next is not None:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
