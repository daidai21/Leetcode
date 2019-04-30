# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr, prev = head, None
        while curr:
            next = curr.next  # 下一节点就是现在的下一个节点
            curr.next = prev  # 现在的下一个节点指针指向前一个节点
            prev = curr  # 前一个指针后移
            curr = next  # 当前指针后移
        return prev  # 最前面节点


'''
三个指针：当前节点、后面节点、前面节点
'''