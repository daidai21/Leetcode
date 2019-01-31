# 暴力 & 将值存在数组
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        len_ = len(tmp)
        for i in range(int(len_ / 2)):
            if tmp[i] != tmp[len_ - i - 1]: return False
        return True
