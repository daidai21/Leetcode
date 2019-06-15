# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def recursion(node):
            return recursion(node.left) + [node.val] + recursion(node.right) if node else []
        
        return recursion(root)[k - 1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0: return root.val
            root = root.right


# 先到最左下根节点，再到最左下根节点的父节点的右子节点
# 若不满足条件，再到这个父节点的父节点
# 再到这个父节点的右子节点
