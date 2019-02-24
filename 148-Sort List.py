# violence
# Runtime: 112 ms, faster than 95.04% of Python3 online submissions for Sort List.
# Memory Usage: 25.5 MB, less than 8.03% of Python3 online submissions for Sort List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        tmp.sort()
        point = head = ListNode(None)
        for value in tmp:
            node = ListNode(value)
            point.next = node
            point = point.next
        return head.next


'''
the first, using a array storage the value of list.
the second, sorting the array.
the last, rebuilding the list.
'''
