# Runtime: 40 ms, faster than 98.69% of Python3 online submissions for Path Sum.
# Memory Usage: 15.1 MB, less than 84.06% of Python3 online submissions for Path Sum.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        left = self.hasPathSum(root.left, sum - root.val) if root.left else False
        right = self.hasPathSum(root.right, sum - root.val) if root.right else False
        return left or right