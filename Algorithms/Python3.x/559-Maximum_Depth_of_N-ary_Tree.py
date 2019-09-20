"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        else:
            next_max_depth = 0
            for next_node in root.children:
                next_max_depth = max(next_max_depth, self.maxDepth(next_node))
            return next_max_depth + 1


# Runtime: 656 ms, faster than 52.09% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 95.1 MB, less than 8.33% of Python3 online submissions for Maximum Depth of N-ary Tree.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        else:
            return max([self.maxDepth(next_node) for next_node in root.children] + [0]) + 1


# Runtime: 700 ms, faster than 10.49% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 95.3 MB, less than 8.33% of Python3 online submissions for Maximum Depth of N-ary Tree.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return 0 if not root else max([self.maxDepth(next_node) for next_node in root.children] + [0]) + 1
