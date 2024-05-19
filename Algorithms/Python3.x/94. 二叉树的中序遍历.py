# 94. 二叉树的中序遍历
# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/

"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, cur):
        if cur is None:
            return
        if cur.left is not None:
            self.dfs(cur.left)
        self.res.append(cur.val)
        if cur.right is not None:
            self.dfs(cur.right)
