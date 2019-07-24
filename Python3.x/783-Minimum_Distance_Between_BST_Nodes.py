# Runtime: 56 ms, faster than 6.06% of Python3 online submissions for Minimum Distance Between BST Nodes.
# Memory Usage: 14 MB, less than 5.03% of Python3 online submissions for Minimum Distance Between BST Nodes.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.tmp = []
        self.recursion(root)
        self.tmp.sort()
        res = float("inf")
        for i in range(1, len(self.tmp)):
            res = min(res, abs(self.tmp[i] - self.tmp[i - 1]))
        return res

    def recursion(self, node):
        if node is None:
            return None
        if node.val:
            self.tmp.append(node.val)
        if node.left:
            self.recursion(node.left)
        if node.right:
            self.recursion(node.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pre = -float("inf")
    res = float("inf")
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res
