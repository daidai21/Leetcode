# Runtime: 660 ms, faster than 74.06% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 95.1 MB, less than 8.33% of Python3 online submissions for N-ary Tree Level Order Traversal.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while len(queue) > 0:
            new_queue = []
            layer_val = []
            for node in queue:
                layer_val.append(node.val)
                new_queue += node.children
            result.append(layer_val)
            queue = new_queue
        return result
