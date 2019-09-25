# Runtime: 56 ms, faster than 99.45% of Python3 online submissions for Recover a Tree From Preorder Traversal.
# Memory Usage: 14.5 MB, less than 25.00% of Python3 online submissions for Recover a Tree From Preorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.values = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", S)][::-1]
        print(self.values)
        return self.recursion(0)

    def recursion(self, level):
        if not self.values or level != self.values[-1][0]:
            return None
        node = TreeNode(self.values.pop()[1])
        node.left  = self.recursion(level + 1)
        node.right = self.recursion(level + 1)
        return node
