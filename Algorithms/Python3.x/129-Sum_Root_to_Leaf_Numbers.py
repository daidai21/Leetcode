# Runtime: 32 ms, faster than 97.15% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 13.8 MB, less than 6.25% of Python3 online submissions for Sum Root to Leaf Numbers.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.recursion(0, root)
        return self.res

    def recursion(self, curr, node):
        if node is None:
            return
        if node.val is not None and node.left is None and node.right is None:
            self.res += curr * 10 + node.val
            return
        self.recursion(curr * 10 + node.val, node.left)
        self.recursion(curr * 10 + node.val, node.right)
