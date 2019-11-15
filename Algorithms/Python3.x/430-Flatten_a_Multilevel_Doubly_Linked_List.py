# dfs
# Runtime: 1060 ms, faster than 11.15% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
# Memory Usage: 354.2 MB, less than 28.57% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dummy = Node(0, None, head, None)
        stack = [head]
        pre = dummy
        while stack:
            root = stack.pop()
            root.prev = pre
            pre.next = root
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            pre = root
        dummy.next.prev = None
        return dummy.next

