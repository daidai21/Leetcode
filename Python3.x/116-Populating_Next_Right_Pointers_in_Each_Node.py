# Runtime: 48 ms, faster than 96.01% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.5 MB, less than 12.72% of Python3 online submissions for Populating Next Right Pointers in Each Node.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        if root.left and root.right:
            self.connect(root.left)
            self.connect(root.right)
            l, r = root.left, root.right
            while l:
                l.next = r
                l, r = l.right, r.left
        return root