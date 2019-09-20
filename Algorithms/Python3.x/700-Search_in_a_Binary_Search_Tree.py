# Runtime: 76 ms, faster than 97.04% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 15.8 MB, less than 9.09% of Python3 online submissions for Search in a Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# Runtime: 80 ms, faster than 87.84% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 15.9 MB, less than 9.09% of Python3 online submissions for Search in a Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or val == root.val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)


# Runtime: 80 ms, faster than 87.84% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 15.6 MB, less than 9.09% of Python3 online submissions for Search in a Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return root if not root or val == root.val else (self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val))
