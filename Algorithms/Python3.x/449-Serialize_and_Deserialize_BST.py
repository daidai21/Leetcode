# Runtime: 64 ms, faster than 66.36% of Python online submissions for Serialize and Deserialize BST.
# Memory Usage: 19.7 MB, less than 58.06% of Python online submissions for Serialize and Deserialize BST.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.vals = []
        self.pre_order(root)
        return ' '.join(map(str, self.vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.vals = collections.deque(map(int, data.split()))
        return self.build(float("-inf"), float("inf"))

    def pre_order(self, node):
        if node:
            self.vals.append(node.val)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def build(self, min_val, max_val):
        if self.vals and min_val < self.vals[0] < max_val:
            val = self.vals.popleft()
            node = TreeNode(val)
            node.left = self.build(min_val, val)
            node.right = self.build(val, max_val)
            return node

        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
