# time: O(n)  space: O(n)
# Runtime: 84 ms, faster than 85.97% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 15.1 MB, less than 2.62% of Python3 online submissions for Convert BST to Greater Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


# 优化
# Runtime: 80 ms, faster than 99.43% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 14.9 MB, less than 2.62% of Python3 online submissions for Convert BST to Greater Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        if not root: return
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)
        return root
