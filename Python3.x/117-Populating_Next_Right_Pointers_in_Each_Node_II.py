# Runtime: 392 ms, faster than 57.37% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 48.4 MB, less than 5.26% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
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
        if not root:
            return root
        self.bfs([root])
        return root

    def bfs(self, layer):
        temp = []
        if not layer:
            return
        for idx, node in enumerate(layer):
            if node.left is not None:
                temp.append(node.left)
            if node.right is not None:
                temp.append(node.right)
            node.next = layer[idx + 1] if idx < len(layer) - 1 else None
        self.bfs(temp)
