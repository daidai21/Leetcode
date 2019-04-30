# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        point = head
        while l1 and l2:
            if l1.val > l2.val:  # 处理小的l2
                tmp = ListNode(l2.val)
                point.next = tmp
                point, l2 = point.next, l2.next
            else:  # 处理小的或者相等的l1
                tmp = ListNode(l1.val)
                point.next = tmp
                point, l1 = point.next, l1.next
        tmp_point = l1 if l1 else l2  # 将剩余的链表直接添加到合并链表的尾部
        point.next = tmp_point
        return head.next

