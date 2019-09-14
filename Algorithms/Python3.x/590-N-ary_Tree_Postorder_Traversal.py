# Runtime: 640 ms, faster than 96.00% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 95.2 MB, less than 7.14% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack += curr.children
        return reversed(res)
