'''
# 暴力求解
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodes = []
        tmp = head = ListNode(None)
        for node in lists:  # 将所有节点加入链表
            while node:
                nodes.append(node.val)
                node = node.next
        for val in sorted(nodes):  # 将所有节点排序，然后再重新建立链表
            tmp.next = ListNode(val)
            tmp = tmp.next
        return head.next
'''
