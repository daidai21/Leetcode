# Runtime: 56 ms, faster than 29.51% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 15.8 MB, less than 29.87% of Python3 online submissions for Minimum Depth of Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = self.minDepth(root.left) + 1 if root.left is not None else float("inf")
        right = self.minDepth(root.right) + 1 if root.right is not None else float("inf")
        return min(left, right)


# Runtime: 48 ms, faster than 82.57% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 14.4 MB, less than 91.69% of Python3 online submissions for Minimum Depth of Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if node:
                if node.left is None and node.right is None:
                    return level
                else:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))