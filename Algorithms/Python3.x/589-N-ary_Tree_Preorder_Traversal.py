# dfs / recursion
# Runtime: 668 ms, faster than 49.97% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 95.3 MB, less than 13.64% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.preorder = []
        self.dfs(root)
        return self.preorder

    def dfs(self, node):
        if not node:
            return 
        else:
            self.preorder.append(node.val)
            for next_node in node.children:
                self.dfs(next_node)


# iteratively
# Runtime: 664 ms, faster than 59.72% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 95.3 MB, less than 13.64% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        preorder = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val is not None:
                preorder.append(node.val)
            if node.children:
                stack += node.children[::-1]
        return preorder
