# Runtime: 64 ms, faster than 63.68% of Python3 online submissions for Unique Binary Search Trees II.
# Memory Usage: 15.1 MB, less than 18.90% of Python3 online submissions for Unique Binary Search Trees II.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node

        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last + 1)
                    for left in trees(first, root - 1)
                    for right in trees(root + 1, last)] or [None]

        return trees(1, n) if n != 0 else []


# Runtime: 68 ms, faster than 35.79% of Python3 online submissions for Unique Binary Search Trees II.
# Memory Usage: 15.1 MB, less than 33.33% of Python3 online submissions for Unique Binary Search Trees II.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate(1, n) if n != 0 else []

    def generate(self, first, last):
        trees = []
        for root in range(first, last + 1):
            for left in self.generate(first, root - 1):
                for right in self.generate(root + 1, last):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees += node,
        return trees or [None]
