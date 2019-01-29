# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = ListNode(None)
        tmp.next = head
        start, end = tmp, tmp
        for _ in range(n): start = start.next
        while start.next:
            start, end = start.next, end.next
        end.next = end.next.next
        return tmp.next


'''
加一个头结点，并使用双指针start和end。
start先向前移动n个节点，然后start和end同时移动，当start.next==None时，此时end.next指的就是需要删除的节点。
'''