# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        res = jump = ListNode(None)
        res.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre
                jump = l
                l = r
            else:
                return res.next


# Runtime: 48 ms, faster than 95.85% of Python3 online submissions for Reverse Nodes in k-Group.
# Memory Usage: 14.2 MB, less than 44.41% of Python3 online submissions for Reverse Nodes in k-Group.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        res = jump = ListNode(None)
        res.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r, count = r.next, count + 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, pre, cur = pre, cur, cur.next
                jump.next, jump, l = pre, l, r
            else:
                return res.next

