# Runtime: 44 ms, faster than 62.95% of Python3 online submissions for Rotate List.
# Memory Usage: 13.9 MB, less than 6.05% of Python3 online submissions for Rotate List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 0:
            return head
        tmp, length = head, 1
        while tmp.next:
            tmp = tmp.next
            length += 1
        k = k % length
        if k == 0:  # don't need rotate
            return head
        fast = slow = head  # fast and slow point
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        res = slow.next # ready result
        slow.next = None
        fast.next = head
        return res
