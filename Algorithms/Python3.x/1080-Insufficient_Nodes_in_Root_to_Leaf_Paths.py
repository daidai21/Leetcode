# recursion
# Runtime: 100 ms, faster than 55.12% of Python3 online submissions for Insufficient Nodes in Root to Leaf Paths.
# Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Insufficient Nodes in Root to Leaf Paths.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root.left == root.right:  # 叶子
            return None if root.val < limit else root  # 判断是否要删除节点
        if root.left:  # 左递归
            root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right:  # 右递归
            root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None  # 返回
