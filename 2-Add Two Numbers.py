# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1 is None and l2 is None: return None
        # if l1 is None: return l2
        # if l2 is None: return l1
        list_ = ListNode(-1)
        point = list_
        flag = 0  # 进位标志
        while l1 and l2:
            add = l1.val + l2.val + flag
            flag = 1 if add >= 10 else 0
            point.next = ListNode(add % 10)
            point = point.next
            l1, l2 = l1.next, l2.next
        l = l1 if l1 else l2
        while l:
            add = l.val + flag
            flag = 1 if add >= 10 else 0
            point.next = ListNode(add % 10)
            point, l = point.next, l.next
        if flag: point.next = ListNode(1)
        return list_.next


'''
常规思路
两个要注意的地方：如果列表长度不相等；如果列表相加完成最后仍有进位位。
'''