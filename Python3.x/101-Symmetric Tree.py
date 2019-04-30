# 递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.judge(root.left, root.right)

    def judge(self, left, right):
        if not left or not right: return left == right
        if left.val != right.val: return False
        return self.judge(left.left, right.right) and self.judge(left.right, right.left)


'''
递归，对于每个节点，检查树的左右节点值是否相等，
同时判断：左节点的左子树和右节点的右子树是否对称、右节点的左子树和左节点的右子树是否对称。
'''