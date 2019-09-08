# Runtime: 2260 ms, faster than 8.33% of Python3 online submissions for Insertion Sort List.
# Memory Usage: 15.6 MB, less than 25.00% of Python3 online submissions for Insertion Sort List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = ListNode(None)
        res.next = head
        old_head = head.next
        head.next = None
        while old_head:
            temp = old_head.next
            # find insert index
            p1 = res
            while p1 and p1.next and p1.next.val < old_head.val:
                p1 = p1.next
            if p1.next is None:
                p1.next = old_head
                old_head.next = None
            else:
                p2 = p1.next
                p1.next = old_head
                old_head.next = p2
            old_head = temp
        return res.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = res = ListNode(None)
        cur = res.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = res
            while p.next.val < val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return res.next
