# Runtime: 32 ms, faster than 90.09% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 7.14% of Python3 online submissions for Middle of the Linked List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
