# Runtime: 44 ms, faster than 99.10% of Python3 online submissions for Path Sum II.
# Memory Usage: 18.8 MB, less than 21.25% of Python3 online submissions for Path Sum II.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        self.dfs([], root, sum)
        return self.res

    def dfs(self, curr, node, sum):
        if node is None:
            return
        if sum - node.val == 0 and node.left is None and node.right is None:
            self.res.append(curr + [node.val])
            return
        if node.left:
            self.dfs(curr + [node.val], node.left, sum - node.val)
        if node.right:
            self.dfs(curr + [node.val], node.right, sum - node.val)
