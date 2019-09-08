# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None: return None
        point_a, point_b = headA, headB
        while point_a is not point_b:
            point_a = point_a.next if point_a is not None else headB
            point_b = point_b.next if point_b is not None else headA
        return point_a


'''
设置两个指针分别从头遍历A和B，当其中一条遍历到末尾时，跳到另一条链表继续遍历。
连个指针终会相等，而且只有两种情况，一种情况是在交点处相遇，另一种情况是在各自的末尾的空节点处相等。

因为两个指针走过的路程相同，是两个链表的长度之和，所以一定会相等。
'''