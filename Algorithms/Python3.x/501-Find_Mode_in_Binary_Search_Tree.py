# Runtime: 60 ms, faster than 80.11% of Python3 online submissions for Find Mode in Binary Search Tree.
# Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Find Mode in Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.val_freq = {}
        self.dfs(root)
        max_freq = max([freq for _, freq in self.val_freq.items()] + [0])
        return [val for val in self.val_freq if self.val_freq[val] == max_freq]

    def dfs(self, node):
        if not node:
            return 
        self.val_freq[node.val] = self.val_freq.get(node.val, 0) + 1
        self.dfs(node.left)
        self.dfs(node.right)


# Runtime: 56 ms, faster than 90.45% of Python3 online submissions for Find Mode in Binary Search Tree.
# Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Find Mode in Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.max_freq = 0
        self.result = []
        self.cur_freq = 0
        self.pre_val = 0
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        self.cur_freq = 1 if node.val != self.pre_val else self.cur_freq + 1
        if self.cur_freq == self.max_freq:
            self.result.append(node.val)
        elif self.cur_freq > self.max_freq:
            self.result = [node.val]
            self.max_freq = self.cur_freq
        self.pre_val = node.val
        self.dfs(node.right)
