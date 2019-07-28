# Runtime: 36 ms, faster than 79.87% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14 MB, less than 5.02% of Python3 online submissions for Reverse Linked List II.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        cur, pre = head, None
        while m > 1:
            pre = cur
            cur = cur.next
            m, n = m - 1, n - 1
        tail, con = cur, pre  # 2 pointer for the final connection
        while n:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            n -= 1
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head
