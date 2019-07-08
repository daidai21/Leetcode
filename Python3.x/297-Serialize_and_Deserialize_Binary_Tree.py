# Runtime: 112 ms, faster than 93.82% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# Memory Usage: 18.2 MB, less than 42.16% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# using string ('#' is None Node)
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
        def recursion(node):
            if node:
                vals.append(str(node.val))
                recursion(node.left)
                recursion(node.right)
            else:
                vals.append('#')

        vals = []
        recursion(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def func():
            val = next(vals)  # next返回迭代器的下一项
            if val == '#': return None
            node = TreeNode(int(val))
            node.left = func()
            node.right = func()
            return node
        vals = iter(data.split())  # iter生成迭代对象
        return func()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
