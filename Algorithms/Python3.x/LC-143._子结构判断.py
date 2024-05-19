# LCR 143. 子结构判断
# https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/description/


"""
给定两棵二叉树 tree1 和 tree2，判断 tree2 是否以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。
注意，空树 不会是以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False
        if A is None and B is None:
            return True
        if A is None:
            return False
        return self.isSame(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isSame(self, a, b):
        if a is None and b is None:
            return True
        if a is None and b is not None:
            return False
        if a is not None and b is None:
            return True
        return a.val == b.val and self.isSame(a.left, b.left) and self.isSame(a.right, b.right)

