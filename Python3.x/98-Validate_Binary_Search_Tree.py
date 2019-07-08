# 先进行递归中序遍历将数据存储到数组，然后检查数组是否升序
# Runtime: 52 ms, faster than 88.79% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15.6 MB, less than 0.99% of Python3 online submissions for Validate Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        tmp = []
        self.inorder_traversal(root, tmp)
        for i in range(1, len(tmp)):
            if tmp[i] <= tmp[i - 1]: return False
        return True

    def inorder_traversal(self, node, tmp):
        if not node: return
        self.inorder_traversal(node.left, tmp)
        tmp.append(node.val)
        self.inorder_traversal(node.left, tmp)


# 递归
# Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 14.9 MB, less than 0.99% of Python3 online submissions for Validate Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        def check_bst(node, left, right):
            if not node: return True
            if not left < node.val < right: return False
            return check_bst(node.left, left, node.val) and check_bst(node.right, node.val, right)

        return check_bst(root, float("-inf"), float("inf"))
