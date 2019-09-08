# Runtime: 40 ms, faster than 64.74% of Python3 online submissions for Sum of Left Leaves.
# Memory Usage: 14.2 MB, less than 7.69% of Python3 online submissions for Sum of Left Leaves.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
